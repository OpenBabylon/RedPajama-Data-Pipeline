from datasets import load_dataset
from pathlib import Path
import random
from tqdm import tqdm

from utilities.io import Writer
from utilities.text.util import generate_paragraphs
import re

def remove_html_tags(text):
    """Remove HTML tags from a string using regex."""
    clean = re.sub(r'<[^>]+>', '', text)
    return clean



class UkrNewsDownloader:
    r""" Loads the RedPajama Books dataset from HuggingFace Datasets and saves
    it to disk """

    dataset_name = "ukrainian_news"
    output_fp = "ukrainian-news/en-books.jsonl.gz"

    def __init__(
            self, lang, out_dir, overwrite, cache_dir, max_samples,
            max_paragraphs_per_sample=200, max_samples_per_book=500
    ):
        self._lang = lang
        self._out_dir = out_dir
        self._overwrite = overwrite
        self._cache_dir = cache_dir
        self._max_samples = max_samples
        self._max_paragraphs_per_sample = max_paragraphs_per_sample
        self._max_samples_per_book = max_samples_per_book
        self._filepath = None

    def __str__(self):
        return f"{self.__class__.__name__}(lang={self._lang})"

    @property
    def filepath(self):
        return self._filepath

    def __generate_chunks(self, text: str):
        text = remove_html_tags(text)

        if self._max_paragraphs_per_sample is None:
            yield text
            return

        n_samples = 0
        buffer = []
        buffer_size = random.randint(1, self._max_paragraphs_per_sample)
        for par in generate_paragraphs(text):
            buffer.append(par)
            if len(buffer) >= buffer_size:
                yield "\n".join(buffer)

                buffer_size = random.randint(
                    1, self._max_paragraphs_per_sample
                )
                buffer = []
                n_samples += 1

                if n_samples >= self._max_samples_per_book > 0:
                    break

    def run(self, logger):

        self._filepath = Path(self._out_dir) / self.output_fp
        logger.info(f"{str(self)} Output file: {self._filepath}")
        logger.info(f"{str(self)} max_samples: {self._max_samples}")

        if self._filepath.exists():
            if not self._overwrite:
                raise FileExistsError(f"File {self._filepath} already exists.")
            else:
                self._filepath.unlink()
                logger.info(f"{str(self)} Deleted {self._filepath}")

        out_uri = "file://" + str(self._filepath)
        writer = Writer(uri=out_uri, schema=[("text", str)])

        logger.info(f"{str(self)} Download start.")
        pbar = tqdm(desc="writing progress", total=self._max_samples)
        flush_every = 5_000

        n_docs = 0
        for book in load_dataset(
                "zeusfsx/ukrainian-news",
                cache_dir=self._cache_dir,
                split="train",
                streaming=True,
                trust_remote_code=True
        ):
            for chunk in self.__generate_chunks(book["text"]):
                n_docs += 1
                if n_docs > self._max_samples > 0:
                    break

                writer.write(
                    data_obj={"text": chunk},
                    flush=n_docs % flush_every == 0
                )
                pbar.update(1)

            else:
                continue
            break

        pbar.close()
        writer.close()
        logger.info(f"{str(self)} Download finished; num_samples={n_docs - 1}")

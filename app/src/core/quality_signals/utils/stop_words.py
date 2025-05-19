"""
The stop words in this file are taken from https://github.com/6/stopwords-json
"""

from typing import Set

__all__ = ["get_stop_words"]


def get_stop_words(lang) -> Set[str]:
    return stop_words[lang]

uk_stopwrods = """а
аби
абиде
абиким
абикого
абиколи
абикому
абикуди
абихто
абичий
абичийого
абичийому
абичим
абичию
абичия
абичиє
абичиєму
абичиєю
абичиєї
абичиї
абичиїй
абичиїм
абичиїми
абичиїх
абичого
абичому
абищо
абияка
абияке
абиякий
абияким
абиякими
абияких
абиякого
абиякому
абиякою
абиякої
абияку
абиякі
абиякій
абиякім
або
абощо
авжеж
авось
ага
ад
адже
аж
ажень
аз
ай
але
ало
амінь
ант
ану
ані
аніде
аніж
анізащо
аніким
анікого
анікогісінько
аніколи
анікому
аніскільки
аніхто
анічим
анічого
анічогісінько
анічому
аніщо
аніяка
аніяке
аніякий
аніяким
аніякими
аніяких
аніякого
аніякому
аніякою
аніякої
аніяку
аніякі
аніякій
аніякім
аніякісенька
аніякісеньке
аніякісенький
аніякісеньким
аніякісенькими
аніякісеньких
аніякісенького
аніякісенькому
аніякісенькою
аніякісенької
аніякісеньку
аніякісенькі
аніякісенькій
аніякісенькім
аніякісінька
аніякісіньке
аніякісінький
аніякісіньким
аніякісінькими
аніякісіньких
аніякісінького
аніякісінькому
аніякісінькою
аніякісінької
аніякісіньку
аніякісінькі
аніякісінькій
аніякісінькім
ат
ато
атож
ау
ах
ач
ачей
аякже
б
ба
багато
багатьма
багатьом
багатьох
баз
бай
бат
бах
бац
баш
бе
беж
без
безперервно
бел
бер
би
бир
бич
близько
близько від
бо
бов
бод
бодай
боз
бош
був
буває
буде
будем
будемо
будете
будеш
буду
будуть
будь
будь ласка
будьмо
будьте
була
були
було
бути
бух
буц
буцім
буцімто
бі
біб
більш
більше
біля
в
в бік
в залежності від
в міру
в напрямі до
в порівнянні з
в процесі
в результаті
в ролі
в силу
в сторону
в супроводі
в ході
в ім'я
в інтересах
вад
важлива
важливе
важливий
важливі
вак
вам
вами
ван
вас
ват
ваш
ваша
ваше
вашим
вашими
ваших
вашого
вашому
вашою
вашої
вашу
ваші
вашій
вашім
ввесь
вві
вгору
вдалині
вед
верх
весь
вех
вже
вздовж
ви
виз
вис
височині
вище 
вйо
власне
властиво
вміти
внаслідок
вниз
внизу
во
вон
вона
вони
воно
восьмий
вперед
вподовж
впоперек
впритиск
впритул
впродовж
впрост
все
всередині
всею
вслід
всупереч
всього
всьому
всю
всюди
вся
всяк
всяка
всяке
всякий
всяким
всякими
всяких
всякого
всякому
всякою
всякої
всяку
всякі
всякій
всякім
всі
всій
всіляка
всіляке
всілякий
всіляким
всілякими
всіляких
всілякого
всілякому
всілякою
всілякої
всіляку
всілякі
всілякій
всілякім
всім
всіма
всіх
всією
всієї
втім
ві
віг
від
від імені
віддалік від
відколи
відносно
відповідно
відповідно до
відсотків
відтепер
відтоді
він
вісім
вісімнадцятий
вісімнадцять
віт
віф
віх
віц
віщо
віщось
г
га
гав
гаразд
ге
гез
гем
геп
гет
геть
гех
ги
гик
гир
гич
гм
го
говорив
гог
гоп
гоц
гу
гуп
д
да
давай
давати
давно
далеко
далеко від
далі
даром
два
двадцятий
двадцять
дванадцятий
дванадцять
двох
дві
де
дев'ятий
дев'ятнадцятий
дев'ятнадцять
дев'ять
дедалі
деким
декого
деколи
декому
декотра
декотре
декотрий
декотрим
декотрими
декотрих
декотрого
декотрому
декотрою
декотрої
декотру
декотрі
декотрій
декотрім
декілька
декільком
декількома
декількох
декім
десь
десятий
десять
дехто
дечий
дечийого
дечийому
дечим
дечию
дечия
дечиє
дечиєму
дечиєю
дечиєї
дечиї
дечиїй
дечиїм
дечиїми
дечиїх
дечого
дечому
дечім
дещо
деяка
деяке
деякий
деяким
деякими
деяких
деякого
деякому
деякою
деякої
деяку
деякі
деякій
деякім
деінде
для
до
добре
довго
довкола
довкіл
дог
доки
допоки
допіру
досить
досі
дотепер
доти
другий
друго
дуже
дякую
дійсно
діл
е
еге
еж
ей
ерг
ест
ет
ех
еч
ж
же
жоден
жодна
жодне
жодний
жодним
жодними
жодних
жодного
жодному
жодною
жодної
жодну
жодні
жодній
жоднім
жоднісінька
жоднісіньке
жоднісінький
жоднісіньким
жоднісінькими
жоднісіньких
жоднісінького
жоднісінькому
жоднісінькою
жоднісінької
жоднісіньку
жоднісінькі
жоднісінькій
жоднісінькім
жуз
з
з метою
з нагоди
з приводу
з розрахунку на
з-за
з-над
з-перед
з-поза
з-поміж
з-понад
з-поперед
з-посеред
з-проміж
з-під
з-серед
за
за винятком
за допомогою
за посередництвом
за рахунок
завгодно
завдяки
завжди
завше
задля
зазвичай
зайнята
зайнятий
зайнято
зайняті
залежно
залежно від
замість
занадто
заради
зараз
зас
зате
збоку
збоку від
зважаючи на
зверх 
зверху
звичайно
звиш
звідки
звідкилясь
звідкись
звідкіль
звідкіля
звідкілясь
звідси
звідсіль
звідсіля
звідти
звідтіль
звідтіля
звідусюди
звідусіль
звідціля
згідно з
здається
здовж
зем
зет
ззаду
зиз
зик
значить
знову
зо
зовсім
зсередини
зух
зі
зіс
и
ич
й
ймовірно
йно
йо
його
йой
йол
йому
йор
йот
йох
к
каже
каз
кар
каф
ках
ке
кед
кет
кеш
кив
кий
кил
ким
кимось
кимсь
ких
киш
коб
коби
кого
когось
кожен
кожна
кожне
кожний
кожним
кожними
кожних
кожного
кожному
кожною
кожної
кожну
кожні
кожній
кожнім
кожнісінька
кожнісіньке
кожнісінький
кожнісіньким
кожнісінькими
кожнісіньких
кожнісінького
кожнісінькому
кожнісінькою
кожнісінької
кожнісіньку
кожнісінькі
кожнісінькій
кожнісінькім
коли
колись
коло
кому
комусь
котра
котрась
котре
котресь
котрий
котрийсь
котрим
котрими
котримись
котримось
котримсь
котрих
котрихось
котрихсь
котрого
котрогось
котрому
котромусь
котрою
котроюсь
котрої
котроїсь
котру
котрусь
котрі
котрій
котрійсь
котрім
котрімсь
котрісь
коц
коч
коштом
край
краще
кру
круг
кругом
крю
кря
крізь
крім
куди
кудись
кудою
кілька
кільком
кількома
кількох
кім
кімось
кімсь
кінець
л
лаж
лап
лас
лат
ле
ледве
ледь
лет
лиш
лише
лишень
лум
луп
лут
льє
люди
людина
ля
лі
ліворуч від
лік
лім
м
мабуть
майже
мало
мати
мац
ме
меж
мене
менше
мені
мерсі
мет
мжа
ми
мимо 
миру
мит
мною
мо
мов
мовби
мовбито
могла
могли
могло
мого
могти
мож
може
можем
можемо
можете
можеш
можна
можу
можуть
можіть
мой
мол
мою
моя
моє
моєму
моєю
моєї
мої
моїй
моїм
моїми
моїх
му
мі
міг
між
мій
мільйонів
н
на
на адресу
на базі
на благо
на випадок
на відміну від
на засадах
на знак
на зразок
на користь
на кшталт
на межі
на основі
на противагу
на підставі
на честь
на чолі
на ґрунті
навколо
навкруг
навкруги 
навкіл
навпаки
навперейми
навпроти
навіть
навіщо
навіщось
нагорі
над
надо
надовкола
надокола
наді
назавжди
назад
назустріч
най
найбільш
нам
нами
наоколо 
наокруг 
наокруги 
наокіл
наперед
напередодні
напереді
наперекір
напереріз
наприкінці
напроти
нарешті
нарівні з
нас
насеред
насподі
наспід
настрічу
насупроти
насупротив 
нате
наче
начеб
начебто
наш
наша
наше
нашим
нашими
наших
нашого
нашому
нашою
нашої
нашу
наші
нашій
нашім
не
не до
не можна
неабичим
неабичого
неабичому
неабищо
небагато
небагатьма
небагатьом
небагатьох
небудь
невважаючи
невже
недалеко
недалеко від
неж
незалежно від
незважаючи
незважаючи на
ней
немає
немов
немовби
немовбито
неначе
неначебто
неподалеку
неподалеку від
неподалечку
неподалечку від
неподалік
неподалік від
нерідко
нех
нехай
нещодавно
нею
неї
нижче
низько
ник
ним
ними
них
нич
но
ну
нуг
нуд
нум
нумо
нумте
ньо
нього
ньому
ню
нюх
ня
няв
ні
ніби
ніби-то
нібито
ніде
ніж
нізащо
нізвідки
нізвідкіля
ній
ніким
нікого
нікогісінько
ніколи
нікому
нікотра
нікотре
нікотрий
нікотрим
нікотрими
нікотрих
нікотрого
нікотрому
нікотрою
нікотрої
нікотру
нікотрі
нікотрій
нікотрім
нікуди
нім
нінащо
ніскільки
ніт
ніхто
нічий
нічийна
нічийне
нічийний
нічийним
нічийними
нічийних
нічийного
нічийному
нічийною
нічийної
нічийну
нічийні
нічийній
нічийнім
нічийого
нічийому
нічим
нічию
нічия
нічиє
нічиєму
нічиєю
нічиєї
нічиї
нічиїй
нічиїм
нічиїми
нічиїх
нічого
нічому
ніщо
ніяк
ніяка
ніяке
ніякий
ніяким
ніякими
ніяких
ніякого
ніякому
ніякою
ніякої
ніяку
ніякі
ніякій
ніякім
ніякісінька
ніякісіньке
ніякісінький
ніякісіньким
ніякісінькими
ніякісіньких
ніякісінького
ніякісінькому
ніякісінькою
ніякісінької
ніякісіньку
ніякісінькі
ніякісінькій
ніякісінькім
о
об
обабіч
обаполи
обидва
обр
обік
обіруч
обіч
ов
од
один
одинадцятий
одинадцять
одна
однак
одначе
одне
одним
одними
одних
одно
одного
одного разу
одному
одною
одної
одну
одні
одній
однім
однією
однієї
ож
ой
окрай
окроме
округ
округи
окрім
окіл
ом
он
онде
онно
оно
оподаль
оподаль від
оподалік
оподалік від
опостін
опостінь
опроче
опріч
опріче
опісля
осе
оскільки
особливо
осторонь
ось
осісьо
от
ота
отак
отака
отаке
отакий
отаким
отакими
отаких
отакого
отакому
отакою
отакої
отаку
отакі
отакій
отакім
отакісінька
отакісіньке
отакісінький
отакісіньким
отакісінькими
отакісіньких
отакісінького
отакісінькому
отакісінькою
отакісінької
отакісіньку
отакісінькі
отакісінькій
отакісінькім
отам
оте
отже
отим
отими
отих
ото
отого
отож
отой
отому
отою
отої
отсе
оттак
отто
оту
отут
оті
отій
отім
отією
отієї
ох
оце
оцей
оцим
оцими
оцих
оцього
оцьому
оцю
оця
оці
оцій
оцім
оцією
оцієї
п
п'я
п'ятий
п'ятнадцятий
п'ятнадцять
п'ять
па
пад
пак
пек
перед
передо
переді
перетака
перетаке
перетакий
перетаким
перетакими
перетаких
перетакого
перетакому
перетакою
перетакої
перетаку
перетакі
перетакій
перетакім
перший
пиж
плі
по
поблизу
побік
побіля
побіч
поверх
повз
повздовж
повинно
повище
повсюди
повсюдно
подаль від
подалі від
подекуди
подеяка
подеяке
подеякий
подеяким
подеякими
подеяких
подеякого
подеякому
подеякою
подеякої
подеяку
подеякі
подеякій
подеякім
подовж
подібно до
поз
поза
позад
позаду
позата
позате
позатим
позатими
позатих
позатого
позатой
позатому
позатою
позатої
позату
позаті
позатій
позатім
позатією
позатієї
позаяк
поздовж
поки
покрай
покіль
помежи
помимо
поміж
помість
понад
понадо
понаді
понижче
пообіч
поодаль від
поодалік від
поперед
попереду
поперек
попліч
попри
попросту
попід
пора
поруч
поряд
поряд з
порівняно з
посеред
посередині
потрібно
потім
поуз
початку
почерез
праворуч від
пред
предо
преді
прекрасно
прецінь
при
притому
причому
причім
про
проз
промеж
проміж
просто
проте
проти
против
противно
протягом
пря
пріч
пхе
пху
пі
пів
півперек
під
під знаком
під приводом
під час
підо
пізніше
пім
пір
після
р
ради
раз
разом з
разу
рано
раніш
раніш від
раніше
раніше від
раптом
ре
рет
риж
рим
рип
роб
року
років
рос
рох
році
рус
рух
руч
рік
с
саж
саз
сак
сам
сама
саме
сами
самий
самим
самими
самих
само
самого
самому
самою
самої
саму
самі
самій
самім
сап
сас
свого
свою
своя
своє
своєму
своєю
своєї
свої
своїй
своїм
своїми
своїх
свій
се
себе
себто
сей
сен
серед
середи
середу
сеч
си
сив
сиг
сиз
сик
сиріч
сих
сказав
сказала
сказати
скрізь
скільки
скільки-то
скількись
скільком
скількома
скількомась
скількомось
скількомсь
скількох
скількохось
скількохсь
сли
слідом за
соб
собою
собі
соп
спасибі
спереду
спочатку
справ
справді
став
стосовно
стільки
стільком
стількома
стількох
су
судячи з
супроти
супротив
суть
суч
суш
сьогодні
сьомий
сюди
ся
сяг
сяк
сяка
сяке
сякий
сяким
сякими
сяких
сякого
сякому
сякою
сякої
сяку
сякі
сякій
сякім
сям
сі
сім
сімнадцятий
сімнадцять
сіп
т
та
таж
так
така
таке
такенна
такенне
такенний
такенним
такенними
такенних
такенного
такенному
такенною
такенної
такенну
такенні
такенній
такеннім
таки
такий
таким
такими
таких
такого
також
такому
такою
такої
таку
такі
такій
такім
такісінька
такісіньке
такісінький
такісіньким
такісінькими
такісіньких
такісінького
такісінькому
такісінькою
такісінької
такісіньку
такісінькі
такісінькій
такісінькім
тал
там
тамки
тамта
тамте
тамтим
тамтими
тамтих
тамтого
тамтой
тамтому
тамтою
тамтої
тамту
тамті
тамтій
тамтім
тамтією
тамтієї
тар
тат
таш
тва
твого
твою
твоя
твоє
твоєму
твоєю
твоєї
твої
твоїй
твоїм
твоїми
твоїх
твій
те
тебе
тег
теж
тем
тепер
теперечки
тес
теф
теє
ти
тик
тил
тим
тими
тисяч
тих
то
тобою
тобто
тобі
того
тоді
тож
той
тол
тому
тому що
тот
тощо
тою
тої
тра
тре
треба
третій
три
тринадцятий
тринадцять
трохи
тс
тсс
ту
туди
тудою
туп
тут
тутеньки
тутечки
тутки
туф
туц
тю
тюг
тюп
тяг
тяж
тям
тяп
ті
тій
тільки
тім
тією
у
у бік
у вигляді
у випадку
у відповідності до
у відповідь на
у залежності від
у зв'язку з
у міру
у напрямі до
у порівнянні з
у процесі
у результаті
у ролі
у силу
у сторону
у супроводі
у ході
ув
увесь
уві
угу
уже
узбіч
уздовж
укр
ум
унаслідок
униз
унизу
унт
уперед
уподовж
упоперек
упритиск до
упритул до
упродовж
упрост
ус
усе
усередині
услід
услід за
усупереч
усього
усьому
усю
усюди
уся
усяк
усяка
усяке
усякий
усяким
усякими
усяких
усякого
усякому
усякою
усякої
усяку
усякі
усякій
усякім
усі
усій
усіляка
усіляке
усілякий
усіляким
усілякими
усіляких
усілякого
усілякому
усілякою
усілякої
усіляку
усілякі
усілякій
усілякім
усім
усіма
усіх
усією
усієї
утім
ух
ф
ф'ю
фа
фаг
фай
фат
фе
фед
фез
фес
фет
фзн
фоб
фот
фра
фру
фу
фук
фур
фус
фіш
х
ха
хаз
хай
хап
хат
хащ
хе
хет
хи
хиб
хм
хо
хов
хол
хон
хоп
хор
хотіти
хоч
хоча
хочеш
хро
хрю
хто
хтось
ху
хуз
хук
хух
хху
хіба
ц
це
цебто
цей
цеп
ци
цим
цими
цир
цих
цло
цоб
цок
цоп
цор
цс
цсс
цуг
цур
цуц
цього
цьому
цю
цюк
ця
цяв
цяп
ці
цід
цій
цім
ціною
цією
цієї
ч
чал
чар
час
часто
частіше
часу
чах
чей
чень
через
четвертий
чи
чий
чийого
чийогось
чийому
чийомусь
чийсь
чик
чим
чимось
чимсь
чир
численна
численне
численний
численним
численними
численних
численні
чию
чиюсь
чия
чиясь
чиє
чиєму
чиємусь
чиєсь
чиєю
чиєюсь
чиєї
чиєїсь
чиї
чиїй
чиїйсь
чиїм
чиїми
чиїмись
чиїмось
чиїмсь
чиїсь
чиїх
чиїхось
чиїхсь
чля
чого
чогось
чом
чому
чомусь
чон
чоп
чортзна
чос
чотири
чотирнадцятий
чотирнадцять
чу
чум
чур
чш
чім
чімось
чімсь
чіт
ш
ша
шаг
шал
шам
шво
шед
шен
шиз
шир
шляхом
шостий
шістнадцятий
шістнадцять
шість
щ
ще
щем
щеп
щип
щир
що
щоб
щоби
щодо
щойно
щоправда
щось
щі
ь
ю
юз
юн
юнь
юс
ют
юхт
я
яв
яд
яз
язь
як
яка
якась
якби
яке
якесь
який
якийсь
яким
якими
якимись
якимось
якимсь
яких
якихось
якихсь
якого
якогось
якому
якомусь
якось
якою
якоюсь
якої
якоїсь
якраз
яку
якусь
якщо
які
якій
якійсь
якім
якімсь
якісь
ял
ям
ян
янь
яо
яп
ярл
ясь
ять
є
єр
єси
і
ібн
ід
із
із-за
із-під
іззаду
ізм
ізсередини
ік
ікс
ікт
ім'я
імовірно
інакша
інакше
інакший
інакшим
інакшими
інакших
інакшого
інакшому
інакшою
інакшої
інакшу
інакші
інакшій
інакшім
інколи
іноді
інша
інше
інший
іншим
іншими
інших
іншого
іншому
іншою
іншої
іншу
інші
іншій
іншім
інь
іч
іще
ї
їдь
їй
їм
їх
їхнього
їхньому
їхньою
їхньої
їхню
їхня
їхнє
їхні
їхній
їхнім
їхніми
їхніх
її"""

stop_words = {
    "bg": {"а", "автентичен", "аз", "ако", "ала", "бе", "без", "беше",
           "би", "бивш", "бивша", "бившо", "бил", "била", "били", "било",
           "благодаря", "близо", "бъдат", "бъде", "бяха", "в", "вас",
           "ваш", "ваша", "вероятно", "вече", "взема", "ви", "вие",
           "винаги", "внимава", "време", "все", "всеки", "всички",
           "всичко", "всяка", "във", "въпреки", "върху", "г", "ги",
           "главен", "главна", "главно", "глас", "го", "година",
           "години", "годишен", "д", "да", "дали", "два", "двама",
           "двамата", "две", "двете", "ден", "днес", "дни", "до",
           "добра", "добре", "добро", "добър", "докато", "докога",
           "дори", "досега", "доста", "друг", "друга", "други", "е",
           "евтин", "едва", "един", "една", "еднаква", "еднакви",
           "еднакъв", "едно", "екип", "ето", "живот", "за", "забавям",
           "зад", "заедно", "заради", "засега", "заспал", "затова",
           "защо", "защото", "и", "из", "или", "им", "има", "имат",
           "иска", "й", "каза", "как", "каква", "какво", "както",
           "какъв", "като", "кога", "когато", "което", "които", "кой",
           "който", "колко", "която", "къде", "където", "към", "лесен",
           "лесно", "ли", "лош", "м", "май", "малко", "ме", "между",
           "мек", "мен", "месец", "ми", "много", "мнозина", "мога",
           "могат", "може", "мокър", "моля", "момента", "му", "н", "на",
           "над", "назад", "най", "направи", "напред", "например", "нас",
           "не", "него", "нещо", "нея", "ни", "ние", "никой", "нито",
           "нищо", "но", "нов", "нова", "нови", "новина", "някои",
           "някой", "няколко", "няма", "обаче", "около", "освен",
           "особено", "от", "отгоре", "отново", "още", "пак", "по",
           "повече", "повечето", "под", "поне", "поради", "после",
           "почти", "прави", "пред", "преди", "през", "при", "пък",
           "първата", "първи", "първо", "пъти", "равен", "равна", "с",
           "са", "сам", "само", "се", "сега", "си", "син", "скоро",
           "след", "следващ", "сме", "смях", "според", "сред", "срещу",
           "сте", "съм", "със", "също", "т", "т.н.", "тази", "така",
           "такива", "такъв", "там", "твой", "те", "тези", "ти", "то",
           "това", "тогава", "този", "той", "толкова", "точно", "три",
           "трябва", "тук", "тъй", "тя", "тях", "у", "утре", "харесва",
           "хиляди", "ч", "часа", "че", "често", "чрез", "ще", "щом",
           "юмрук", "я", "як"},
    "de": {"Ernst", "Ordnung", "Schluss", "a", "ab", "aber", "ach", "acht",
           "achte", "achten", "achter", "achtes", "ag", "alle", "allein",
           "allem", "allen", "aller", "allerdings", "alles", "allgemeinen",
           "als", "also", "am", "an", "andere", "anderen", "andern", "anders",
           "au", "auch", "auf", "aus", "ausser", "ausserdem", "außer",
           "außerdem", "b", "bald", "bei", "beide", "beiden", "beim",
           "beispiel", "bekannt", "bereits", "besonders", "besser", "besten",
           "bin", "bis", "bisher", "bist", "c", "d", "d.h", "da", "dabei",
           "dadurch", "dafür", "dagegen", "daher", "dahin", "dahinter",
           "damals", "damit", "danach", "daneben", "dank", "dann", "daran",
           "darauf", "daraus", "darf", "darfst", "darin", "darum", "darunter",
           "darüber", "das", "dasein", "daselbst", "dass", "dasselbe", "davon",
           "davor", "dazu", "dazwischen", "daß", "dein", "deine", "deinem",
           "deiner", "dem", "dementsprechend", "demgegenüber", "demgemäss",
           "demgemäß", "demselben", "demzufolge", "den", "denen", "denn",
           "denselben", "der", "deren", "derjenige", "derjenigen", "dermassen",
           "dermaßen", "derselbe", "derselben", "des", "deshalb", "desselben",
           "dessen", "deswegen", "dich", "die", "diejenige", "diejenigen",
           "dies", "diese", "dieselbe", "dieselben", "diesem", "diesen",
           "dieser", "dieses", "dir", "doch", "dort", "drei", "drin", "dritte",
           "dritten", "dritter", "drittes", "du", "durch", "durchaus",
           "durfte", "durften", "dürfen", "dürft", "e", "eben", "ebenso",
           "ehrlich", "ei", "ei,", "eigen", "eigene", "eigenen", "eigener",
           "eigenes", "ein", "einander", "eine", "einem", "einen", "einer",
           "eines", "einige", "einigen", "einiger", "einiges", "einmal",
           "eins", "elf", "en", "ende", "endlich", "entweder", "er", "erst",
           "erste", "ersten", "erster", "erstes", "es", "etwa", "etwas",
           "euch", "euer", "eure", "f", "folgende", "früher", "fünf", "fünfte",
           "fünften", "fünfter", "fünftes", "für", "g", "gab", "ganz", "ganze",
           "ganzen", "ganzer", "ganzes", "gar", "gedurft", "gegen",
           "gegenüber", "gehabt", "gehen", "geht", "gekannt", "gekonnt",
           "gemacht", "gemocht", "gemusst", "genug", "gerade", "gern",
           "gesagt", "geschweige", "gewesen", "gewollt", "geworden", "gibt",
           "ging", "gleich", "gott", "gross", "grosse", "grossen", "grosser",
           "grosses", "groß", "große", "großen", "großer", "großes", "gut",
           "gute", "guter", "gutes", "h", "habe", "haben", "habt", "hast",
           "hat", "hatte", "hatten", "hattest", "hattet", "heisst", "her",
           "heute", "hier", "hin", "hinter", "hoch", "hätte", "hätten", "i",
           "ich", "ihm", "ihn", "ihnen", "ihr", "ihre", "ihrem", "ihren",
           "ihrer", "ihres", "im", "immer", "in", "indem", "infolgedessen",
           "ins", "irgend", "ist", "j", "ja", "jahr", "jahre", "jahren", "je",
           "jede", "jedem", "jeden", "jeder", "jedermann", "jedermanns",
           "jedes", "jedoch", "jemand", "jemandem", "jemanden", "jene",
           "jenem", "jenen", "jener", "jenes", "jetzt", "k", "kam", "kann",
           "kannst", "kaum", "kein", "keine", "keinem", "keinen", "keiner",
           "kleine", "kleinen", "kleiner", "kleines", "kommen", "kommt",
           "konnte", "konnten", "kurz", "können", "könnt", "könnte", "l",
           "lang", "lange", "leicht", "leide", "lieber", "los", "m", "machen",
           "macht", "machte", "mag", "magst", "mahn", "mal", "man", "manche",
           "manchem", "manchen", "mancher", "manches", "mann", "mehr", "mein",
           "meine", "meinem", "meinen", "meiner", "meines", "mensch",
           "menschen", "mich", "mir", "mit", "mittel", "mochte", "mochten",
           "morgen", "muss", "musst", "musste", "mussten", "muß", "mußt",
           "möchte", "mögen", "möglich", "mögt", "müssen", "müsst", "müßt",
           "n", "na", "nach", "nachdem", "nahm", "natürlich", "neben", "nein",
           "neue", "neuen", "neun", "neunte", "neunten", "neunter", "neuntes",
           "nicht", "nichts", "nie", "niemand", "niemandem", "niemanden",
           "noch", "nun", "nur", "o", "ob", "oben", "oder", "offen", "oft",
           "ohne", "p", "q", "r", "recht", "rechte", "rechten", "rechter",
           "rechtes", "richtig", "rund", "s", "sa", "sache", "sagt", "sagte",
           "sah", "satt", "schlecht", "schon", "sechs", "sechste", "sechsten",
           "sechster", "sechstes", "sehr", "sei", "seid", "seien", "sein",
           "seine", "seinem", "seinen", "seiner", "seines", "seit", "seitdem",
           "selbst", "sich", "sie", "sieben", "siebente", "siebenten",
           "siebenter", "siebentes", "sind", "so", "solang", "solche",
           "solchem", "solchen", "solcher", "solches", "soll", "sollen",
           "sollst", "sollt", "sollte", "sollten", "sondern", "sonst",
           "soweit", "sowie", "später", "startseite", "statt", "steht",
           "suche", "t", "tag", "tage", "tagen", "tat", "teil", "tel", "tritt",
           "trotzdem", "tun", "u", "uhr", "um", "und", "und?", "uns", "unser",
           "unsere", "unserer", "unter", "v", "vergangenen", "viel", "viele",
           "vielem", "vielen", "vielleicht", "vier", "vierte", "vierten",
           "vierter", "viertes", "vom", "von", "vor", "w", "wahr?", "wann",
           "war", "waren", "wart", "warum", "was", "wegen", "weil", "weit",
           "weiter", "weitere", "weiteren", "weiteres", "welche", "welchem",
           "welchen", "welcher", "welches", "wem", "wen", "wenig", "wenige",
           "weniger", "weniges", "wenigstens", "wenn", "wer", "werde",
           "werden", "werdet", "weshalb", "wessen", "wie", "wieder", "wieso",
           "will", "willst", "wir", "wird", "wirklich", "wirst", "wissen",
           "wo", "wohl", "wollen", "wollt", "wollte", "wollten", "worden",
           "wurde", "wurden", "während", "währenddem", "währenddessen", "wäre",
           "würde", "würden", "x", "y", "z", "z.b", "zehn", "zehnte",
           "zehnten", "zehnter", "zehntes", "zeit", "zu", "zuerst", "zugleich",
           "zum", "zunächst", "zur", "zurück", "zusammen", "zwanzig", "zwar",
           "zwei", "zweite", "zweiten", "zweiter", "zweites", "zwischen",
           "zwölf", "über", "überhaupt", "übrigens"},
    "en": {"a", "a's", "able", "about", "above", "according", "accordingly",
           "across", "actually", "after", "afterwards", "again", "against",
           "ain't", "all", "allow", "allows", "almost", "alone", "along",
           "already", "also", "although", "always", "am", "among", "amongst",
           "an", "and", "another", "any", "anybody", "anyhow", "anyone",
           "anything", "anyway", "anyways", "anywhere", "apart", "appear",
           "appreciate", "appropriate", "are", "aren't", "around", "as",
           "aside", "ask", "asking", "associated", "at", "available", "away",
           "awfully", "b", "be", "became", "because", "become", "becomes",
           "becoming", "been", "before", "beforehand", "behind", "being",
           "believe", "below", "beside", "besides", "best", "better",
           "between", "beyond", "both", "brief", "but", "by", "c", "c'mon",
           "c's", "came", "can", "can't", "cannot", "cant", "cause", "causes",
           "certain", "certainly", "changes", "clearly", "co", "com", "come",
           "comes", "concerning", "consequently", "consider", "considering",
           "contain", "containing", "contains", "corresponding", "could",
           "couldn't", "course", "currently", "d", "definitely", "described",
           "despite", "did", "didn't", "different", "do", "does", "doesn't",
           "doing", "don't", "done", "down", "downwards", "during", "e",
           "each", "edu", "eg", "eight", "either", "else", "elsewhere",
           "enough", "entirely", "especially", "et", "etc", "even", "ever",
           "every", "everybody", "everyone", "everything", "everywhere", "ex",
           "exactly", "example", "except", "f", "far", "few", "fifth", "first",
           "five", "followed", "following", "follows", "for", "former",
           "formerly", "forth", "four", "from", "further", "furthermore", "g",
           "get", "gets", "getting", "given", "gives", "go", "goes", "going",
           "gone", "got", "gotten", "greetings", "h", "had", "hadn't",
           "happens", "hardly", "has", "hasn't", "have", "haven't", "having",
           "he", "he's", "hello", "help", "hence", "her", "here", "here's",
           "hereafter", "hereby", "herein", "hereupon", "hers", "herself",
           "hi", "him", "himself", "his", "hither", "hopefully", "how",
           "howbeit", "however", "i", "i'd", "i'll", "i'm", "i've", "ie", "if",
           "ignored", "immediate", "in", "inasmuch", "inc", "indeed",
           "indicate", "indicated", "indicates", "inner", "insofar", "instead",
           "into", "inward", "is", "isn't", "it", "it'd", "it'll", "it's",
           "its", "itself", "j", "just", "k", "keep", "keeps", "kept", "know",
           "known", "knows", "l", "last", "lately", "later", "latter",
           "latterly", "least", "less", "lest", "let", "let's", "like",
           "liked", "likely", "little", "look", "looking", "looks", "ltd", "m",
           "mainly", "many", "may", "maybe", "me", "mean", "meanwhile",
           "merely", "might", "more", "moreover", "most", "mostly", "much",
           "must", "my", "myself", "n", "name", "namely", "nd", "near",
           "nearly", "necessary", "need", "needs", "neither", "never",
           "nevertheless", "new", "next", "nine", "no", "nobody", "non",
           "none", "noone", "nor", "normally", "not", "nothing", "novel",
           "now", "nowhere", "o", "obviously", "of", "off", "often", "oh",
           "ok", "okay", "old", "on", "once", "one", "ones", "only", "onto",
           "or", "other", "others", "otherwise", "ought", "our", "ours",
           "ourselves", "out", "outside", "over", "overall", "own", "p",
           "particular", "particularly", "per", "perhaps", "placed", "please",
           "plus", "possible", "presumably", "probably", "provides", "q",
           "que", "quite", "qv", "r", "rather", "rd", "re", "really",
           "reasonably", "regarding", "regardless", "regards", "relatively",
           "respectively", "right", "s", "said", "same", "saw", "say",
           "saying", "says", "second", "secondly", "see", "seeing", "seem",
           "seemed", "seeming", "seems", "seen", "self", "selves", "sensible",
           "sent", "serious", "seriously", "seven", "several", "shall", "she",
           "should", "shouldn't", "since", "six", "so", "some", "somebody",
           "somehow", "someone", "something", "sometime", "sometimes",
           "somewhat", "somewhere", "soon", "sorry", "specified", "specify",
           "specifying", "still", "sub", "such", "sup", "sure", "t", "t's",
           "take", "taken", "tell", "tends", "th", "than", "thank", "thanks",
           "thanx", "that", "that's", "thats", "the", "their", "theirs",
           "them", "themselves", "then", "thence", "there", "there's",
           "thereafter", "thereby", "therefore", "therein", "theres",
           "thereupon", "these", "they", "they'd", "they'll", "they're",
           "they've", "think", "third", "this", "thorough", "thoroughly",
           "those", "though", "three", "through", "throughout", "thru", "thus",
           "to", "together", "too", "took", "toward", "towards", "tried",
           "tries", "truly", "try", "trying", "twice", "two", "u", "un",
           "under", "unfortunately", "unless", "unlikely", "until", "unto",
           "up", "upon", "us", "use", "used", "useful", "uses", "using",
           "usually", "uucp", "v", "value", "various", "very", "via", "viz",
           "vs", "w", "want", "wants", "was", "wasn't", "way", "we", "we'd",
           "we'll", "we're", "we've", "welcome", "well", "went", "were",
           "weren't", "what", "what's", "whatever", "when", "whence",
           "whenever", "where", "where's", "whereafter", "whereas", "whereby",
           "wherein", "whereupon", "wherever", "whether", "which", "while",
           "whither", "who", "who's", "whoever", "whole", "whom", "whose",
           "why", "will", "willing", "wish", "with", "within", "without",
           "won't", "wonder", "would", "wouldn't", "x", "y", "yes", "yet",
           "you", "you'd", "you'll", "you're", "you've", "your", "yours",
           "yourself", "yourselves", "z", "zero"},
    "es": {"a", "actualmente", "acuerdo", "adelante", "ademas", "además",
           "adrede", "afirmó", "agregó", "ahi", "ahora", "ahí", "al", "algo",
           "alguna", "algunas", "alguno", "algunos", "algún", "alli", "allí",
           "alrededor", "ambos", "ampleamos", "antano", "antaño", "ante",
           "anterior", "antes", "apenas", "aproximadamente", "aquel",
           "aquella", "aquellas", "aquello", "aquellos", "aqui", "aquél",
           "aquélla", "aquéllas", "aquéllos", "aquí", "arriba", "arribaabajo",
           "aseguró", "asi", "así", "atras", "aun", "aunque", "ayer", "añadió",
           "aún", "b", "bajo", "bastante", "bien", "breve", "buen", "buena",
           "buenas", "bueno", "buenos", "c", "cada", "casi", "cerca", "cierta",
           "ciertas", "cierto", "ciertos", "cinco", "claro", "comentó", "como",
           "con", "conmigo", "conocer", "conseguimos", "conseguir",
           "considera", "consideró", "consigo", "consigue", "consiguen",
           "consigues", "contigo", "contra", "cosas", "creo", "cual", "cuales",
           "cualquier", "cuando", "cuanta", "cuantas", "cuanto", "cuantos",
           "cuatro", "cuenta", "cuál", "cuáles", "cuándo", "cuánta", "cuántas",
           "cuánto", "cuántos", "cómo", "d", "da", "dado", "dan", "dar", "de",
           "debajo", "debe", "deben", "debido", "decir", "dejó", "del",
           "delante", "demasiado", "demás", "dentro", "deprisa", "desde",
           "despacio", "despues", "después", "detras", "detrás", "dia", "dias",
           "dice", "dicen", "dicho", "dieron", "diferente", "diferentes",
           "dijeron", "dijo", "dio", "donde", "dos", "durante", "día", "días",
           "dónde", "e", "ejemplo", "el", "ella", "ellas", "ello", "ellos",
           "embargo", "empleais", "emplean", "emplear", "empleas", "empleo",
           "en", "encima", "encuentra", "enfrente", "enseguida", "entonces",
           "entre", "era", "eramos", "eran", "eras", "eres", "es", "esa",
           "esas", "ese", "eso", "esos", "esta", "estaba", "estaban", "estado",
           "estados", "estais", "estamos", "estan", "estar", "estará", "estas",
           "este", "esto", "estos", "estoy", "estuvo", "está", "están", "ex",
           "excepto", "existe", "existen", "explicó", "expresó", "f", "fin",
           "final", "fue", "fuera", "fueron", "fui", "fuimos", "g", "general",
           "gran", "grandes", "gueno", "h", "ha", "haber", "habia", "habla",
           "hablan", "habrá", "había", "habían", "hace", "haceis", "hacemos",
           "hacen", "hacer", "hacerlo", "haces", "hacia", "haciendo", "hago",
           "han", "hasta", "hay", "haya", "he", "hecho", "hemos", "hicieron",
           "hizo", "horas", "hoy", "hubo", "i", "igual", "incluso", "indicó",
           "informo", "informó", "intenta", "intentais", "intentamos",
           "intentan", "intentar", "intentas", "intento", "ir", "j", "junto",
           "k", "l", "la", "lado", "largo", "las", "le", "lejos", "les",
           "llegó", "lleva", "llevar", "lo", "los", "luego", "lugar", "m",
           "mal", "manera", "manifestó", "mas", "mayor", "me", "mediante",
           "medio", "mejor", "mencionó", "menos", "menudo", "mi", "mia",
           "mias", "mientras", "mio", "mios", "mis", "misma", "mismas",
           "mismo", "mismos", "modo", "momento", "mucha", "muchas", "mucho",
           "muchos", "muy", "más", "mí", "mía", "mías", "mío", "míos", "n",
           "nada", "nadie", "ni", "ninguna", "ningunas", "ninguno", "ningunos",
           "ningún", "no", "nos", "nosotras", "nosotros", "nuestra",
           "nuestras", "nuestro", "nuestros", "nueva", "nuevas", "nuevo",
           "nuevos", "nunca", "o", "ocho", "os", "otra", "otras", "otro",
           "otros", "p", "pais", "para", "parece", "parte", "partir", "pasada",
           "pasado", "paìs", "peor", "pero", "pesar", "poca", "pocas", "poco",
           "pocos", "podeis", "podemos", "poder", "podria", "podriais",
           "podriamos", "podrian", "podrias", "podrá", "podrán", "podría",
           "podrían", "poner", "por", "porque", "posible", "primer", "primera",
           "primero", "primeros", "principalmente", "pronto", "propia",
           "propias", "propio", "propios", "proximo", "próximo", "próximos",
           "pudo", "pueda", "puede", "pueden", "puedo", "pues", "q", "qeu",
           "que", "quedó", "queremos", "quien", "quienes", "quiere", "quiza",
           "quizas", "quizá", "quizás", "quién", "quiénes", "qué", "r",
           "raras", "realizado", "realizar", "realizó", "repente", "respecto",
           "s", "sabe", "sabeis", "sabemos", "saben", "saber", "sabes",
           "salvo", "se", "sea", "sean", "segun", "segunda", "segundo",
           "según", "seis", "ser", "sera", "será", "serán", "sería", "señaló",
           "si", "sido", "siempre", "siendo", "siete", "sigue", "siguiente",
           "sin", "sino", "sobre", "sois", "sola", "solamente", "solas",
           "solo", "solos", "somos", "son", "soy", "soyos", "su", "supuesto",
           "sus", "suya", "suyas", "suyo", "sé", "sí", "sólo", "t", "tal",
           "tambien", "también", "tampoco", "tan", "tanto", "tarde", "te",
           "temprano", "tendrá", "tendrán", "teneis", "tenemos", "tener",
           "tenga", "tengo", "tenido", "tenía", "tercera", "ti", "tiempo",
           "tiene", "tienen", "toda", "todas", "todavia", "todavía", "todo",
           "todos", "total", "trabaja", "trabajais", "trabajamos", "trabajan",
           "trabajar", "trabajas", "trabajo", "tras", "trata", "través",
           "tres", "tu", "tus", "tuvo", "tuya", "tuyas", "tuyo", "tuyos", "tú",
           "u", "ultimo", "un", "una", "unas", "uno", "unos", "usa", "usais",
           "usamos", "usan", "usar", "usas", "uso", "usted", "ustedes", "v",
           "va", "vais", "valor", "vamos", "van", "varias", "varios", "vaya",
           "veces", "ver", "verdad", "verdadera", "verdadero", "vez",
           "vosotras", "vosotros", "voy", "vuestra", "vuestras", "vuestro",
           "vuestros", "w", "x", "y", "ya", "yo", "z", "él", "ésa", "ésas",
           "ése", "ésos", "ésta", "éstas", "éste", "éstos", "última",
           "últimas", "último", "últimos"},
    "fi": {"aiemmin", "aika", "aikaa", "aikaan", "aikaisemmin", "aikaisin",
           "aikajen", "aikana", "aikoina", "aikoo", "aikovat", "aina",
           "ainakaan", "ainakin", "ainoa", "ainoat", "aiomme", "aion",
           "aiotte", "aist", "aivan", "ajan", "alas", "alemmas", "alkuisin",
           "alkuun", "alla", "alle", "aloitamme", "aloitan", "aloitat",
           "aloitatte", "aloitattivat", "aloitettava", "aloitettevaksi",
           "aloitettu", "aloitimme", "aloitin", "aloitit", "aloititte",
           "aloittaa", "aloittamatta", "aloitti", "aloittivat", "alta",
           "aluksi", "alussa", "alusta", "annettavaksi", "annetteva",
           "annettu", "ansiosta", "antaa", "antamatta", "antoi", "aoua", "apu",
           "asia", "asiaa", "asian", "asiasta", "asiat", "asioiden",
           "asioihin", "asioita", "asti", "avuksi", "avulla", "avun", "avutta",
           "edelle", "edelleen", "edellä", "edeltä", "edemmäs", "edes",
           "edessä", "edestä", "ehkä", "ei", "eikä", "eilen", "eivät", "eli",
           "ellei", "elleivät", "ellemme", "ellen", "ellet", "ellette", "emme",
           "en", "enemmän", "eniten", "ennen", "ensi", "ensimmäinen",
           "ensimmäiseksi", "ensimmäisen", "ensimmäisenä", "ensimmäiset",
           "ensimmäisiksi", "ensimmäisinä", "ensimmäisiä", "ensimmäistä",
           "ensin", "entinen", "entisen", "entisiä", "entisten", "entistä",
           "enää", "eri", "erittäin", "erityisesti", "eräiden", "eräs",
           "eräät", "esi", "esiin", "esillä", "esimerkiksi", "et", "eteen",
           "etenkin", "etessa", "ette", "ettei", "että", "haikki", "halua",
           "haluaa", "haluamatta", "haluamme", "haluan", "haluat", "haluatte",
           "haluavat", "halunnut", "halusi", "halusimme", "halusin", "halusit",
           "halusitte", "halusivat", "halutessa", "haluton", "he", "hei",
           "heidän", "heihin", "heille", "heiltä", "heissä", "heistä", "heitä",
           "helposti", "heti", "hetkellä", "hieman", "hitaasti", "hoikein",
           "huolimatta", "huomenna", "hyvien", "hyviin", "hyviksi", "hyville",
           "hyviltä", "hyvin", "hyvinä", "hyvissä", "hyvistä", "hyviä", "hyvä",
           "hyvät", "hyvää", "hän", "häneen", "hänelle", "hänellä", "häneltä",
           "hänen", "hänessä", "hänestä", "hänet", "ihan", "ilman",
           "ilmeisesti", "itse", "itsensä", "itseään", "ja", "jo", "johon",
           "joiden", "joihin", "joiksi", "joilla", "joille", "joilta",
           "joissa", "joista", "joita", "joka", "jokainen", "jokin", "joko",
           "joku", "jolla", "jolle", "jolloin", "jolta", "jompikumpi", "jonka",
           "jonkin", "jonne", "joo", "jopa", "jos", "joskus", "jossa", "josta",
           "jota", "jotain", "joten", "jotenkin", "jotenkuten", "jotka",
           "jotta", "jouduimme", "jouduin", "jouduit", "jouduitte", "joudumme",
           "joudun", "joudutte", "joukkoon", "joukossa", "joukosta", "joutua",
           "joutui", "joutuivat", "joutumaan", "joutuu", "joutuvat", "juuri",
           "jälkeen", "jälleen", "jää", "kahdeksan", "kahdeksannen",
           "kahdella", "kahdelle", "kahdelta", "kahden", "kahdessa",
           "kahdesta", "kahta", "kahteen", "kai", "kaiken", "kaikille",
           "kaikilta", "kaikkea", "kaikki", "kaikkia", "kaikkiaan",
           "kaikkialla", "kaikkialle", "kaikkialta", "kaikkien", "kaikkin",
           "kaksi", "kannalta", "kannattaa", "kanssa", "kanssaan", "kanssamme",
           "kanssani", "kanssanne", "kanssasi", "kauan", "kauemmas", "kaukana",
           "kautta", "kehen", "keiden", "keihin", "keiksi", "keille", "keillä",
           "keiltä", "keinä", "keissä", "keistä", "keitten", "keittä", "keitä",
           "keneen", "keneksi", "kenelle", "kenellä", "keneltä", "kenen",
           "kenenä", "kenessä", "kenestä", "kenet", "kenettä", "kennessästä",
           "kenties", "kerran", "kerta", "kertaa", "keskellä", "kesken",
           "keskimäärin", "ketkä", "ketä", "kiitos", "kohti", "koko",
           "kokonaan", "kolmas", "kolme", "kolmen", "kolmesti", "koska",
           "koskaan", "kovin", "kuin", "kuinka", "kuinkan", "kuitenkaan",
           "kuitenkin", "kuka", "kukaan", "kukin", "kukka", "kumpainen",
           "kumpainenkaan", "kumpi", "kumpikaan", "kumpikin", "kun", "kuten",
           "kuuden", "kuusi", "kuutta", "kylliksi", "kyllä", "kymmenen",
           "kyse", "liian", "liki", "lisäksi", "lisää", "lla", "luo", "luona",
           "lähekkäin", "lähelle", "lähellä", "läheltä", "lähemmäs", "lähes",
           "lähinnä", "lähtien", "läpi", "mahdollisimman", "mahdollista", "me",
           "meidän", "meille", "meillä", "melkein", "melko", "menee", "meneet",
           "menemme", "menen", "menet", "menette", "menevät", "meni",
           "menimme", "menin", "menit", "menivät", "mennessä", "mennyt",
           "menossa", "mihin", "mikin", "miksi", "mikä", "mikäli", "mikään",
           "milloin", "milloinkan", "minne", "minun", "minut", "minä", "missä",
           "mistä", "miten", "mitä", "mitään", "moi", "molemmat", "mones",
           "monesti", "monet", "moni", "moniaalla", "moniaalle", "moniaalta",
           "monta", "muassa", "muiden", "muita", "muka", "mukaan", "mukaansa",
           "mukana", "mutta", "muu", "muualla", "muualle", "muualta",
           "muuanne", "muulloin", "muun", "muut", "muuta", "muutama",
           "muutaman", "muuten", "myöhemmin", "myös", "myöskin", "myöskään",
           "myötä", "ne", "neljä", "neljän", "neljää", "niiden", "niin",
           "niistä", "niitä", "noin", "nopeammin", "nopeasti", "nopeiten",
           "nro", "nuo", "nyt", "näiden", "näin", "näissä", "näissähin",
           "näissälle", "näissältä", "näissästä", "näitä", "nämä", "ohi",
           "oikea", "oikealla", "oikein", "ole", "olemme", "olen", "olet",
           "olette", "oleva", "olevan", "olevat", "oli", "olimme", "olin",
           "olisi", "olisimme", "olisin", "olisit", "olisitte", "olisivat",
           "olit", "olitte", "olivat", "olla", "olleet", "olli", "ollut",
           "oma", "omaa", "omaan", "omaksi", "omalle", "omalta", "oman",
           "omassa", "omat", "omia", "omien", "omiin", "omiksi", "omille",
           "omilta", "omissa", "omista", "on", "onkin", "onko", "ovat",
           "paikoittain", "paitsi", "pakosti", "paljon", "paremmin", "parempi",
           "parhaillaan", "parhaiten", "perusteella", "peräti", "pian",
           "pieneen", "pieneksi", "pienelle", "pienellä", "pieneltä",
           "pienempi", "pienestä", "pieni", "pienin", "puolesta", "puolestaan",
           "päälle", "runsaasti", "saakka", "sadam", "sama", "samaa", "samaan",
           "samalla", "samallalta", "samallassa", "samallasta", "saman",
           "samat", "samoin", "sata", "sataa", "satojen", "se", "seitsemän",
           "sekä", "sen", "seuraavat", "siellä", "sieltä", "siihen", "siinä",
           "siis", "siitä", "sijaan", "siksi", "silloin", "sillä", "silti",
           "sinne", "sinua", "sinulle", "sinulta", "sinun", "sinussa",
           "sinusta", "sinut", "sinä", "sisäkkäin", "sisällä", "siten",
           "sitten", "sitä", "ssa", "sta", "suoraan", "suuntaan", "suuren",
           "suuret", "suuri", "suuria", "suurin", "suurten", "taa", "taas",
           "taemmas", "tahansa", "tai", "takaa", "takaisin", "takana", "takia",
           "tapauksessa", "tarpeeksi", "tavalla", "tavoitteena", "te",
           "tietysti", "todella", "toinen", "toisaalla", "toisaalle",
           "toisaalta", "toiseen", "toiseksi", "toisella", "toiselle",
           "toiselta", "toisemme", "toisen", "toisensa", "toisessa",
           "toisesta", "toista", "toistaiseksi", "toki", "tosin", "tuhannen",
           "tuhat", "tule", "tulee", "tulemme", "tulen", "tulet", "tulette",
           "tulevat", "tulimme", "tulin", "tulisi", "tulisimme", "tulisin",
           "tulisit", "tulisitte", "tulisivat", "tulit", "tulitte", "tulivat",
           "tulla", "tulleet", "tullut", "tuntuu", "tuo", "tuolla", "tuolloin",
           "tuolta", "tuonne", "tuskin", "tykö", "tähän", "tällä", "tällöin",
           "tämä", "tämän", "tänne", "tänä", "tänään", "tässä", "tästä",
           "täten", "tätä", "täysin", "täytyvät", "täytyy", "täällä", "täältä",
           "ulkopuolella", "usea", "useasti", "useimmiten", "usein", "useita",
           "uudeksi", "uudelleen", "uuden", "uudet", "uusi", "uusia", "uusien",
           "uusinta", "uuteen", "uutta", "vaan", "vahemmän", "vai",
           "vaiheessa", "vaikea", "vaikean", "vaikeat", "vaikeilla",
           "vaikeille", "vaikeilta", "vaikeissa", "vaikeista", "vaikka",
           "vain", "varmasti", "varsin", "varsinkin", "varten", "vasen",
           "vasenmalla", "vasta", "vastaan", "vastakkain", "vastan", "verran",
           "vielä", "vierekkäin", "vieressä", "vieri", "viiden", "viime",
           "viimeinen", "viimeisen", "viimeksi", "viisi", "voi", "voidaan",
           "voimme", "voin", "voisi", "voit", "voitte", "voivat", "vuoden",
           "vuoksi", "vuosi", "vuosien", "vuosina", "vuotta", "vähemmän",
           "vähintään", "vähiten", "vähän", "välillä", "yhdeksän", "yhden",
           "yhdessä", "yhteen", "yhteensä", "yhteydessä", "yhteyteen", "yhtä",
           "yhtäälle", "yhtäällä", "yhtäältä", "yhtään", "yhä", "yksi",
           "yksin", "yksittäin", "yleensä", "ylemmäs", "yli", "ylös", "ympäri",
           "älköön", "älä"},
    "fr": {"a", "abord", "absolument", "afin", "ah", "ai", "aie", "ailleurs",
           "ainsi", "ait", "allaient", "allo", "allons", "allô", "alors",
           "anterieur", "anterieure", "anterieures", "apres", "après", "as",
           "assez", "attendu", "au", "aucun", "aucune", "aujourd",
           "aujourd'hui", "aupres", "auquel", "aura", "auraient", "aurait",
           "auront", "aussi", "autre", "autrefois", "autrement", "autres",
           "autrui", "aux", "auxquelles", "auxquels", "avaient", "avais",
           "avait", "avant", "avec", "avoir", "avons", "ayant", "b", "bah",
           "bas", "basee", "bat", "beau", "beaucoup", "bien", "bigre", "boum",
           "bravo", "brrr", "c", "car", "ce", "ceci", "cela", "celle",
           "celle-ci", "celle-là", "celles", "celles-ci", "celles-là", "celui",
           "celui-ci", "celui-là", "cent", "cependant", "certain", "certaine",
           "certaines", "certains", "certes", "ces", "cet", "cette", "ceux",
           "ceux-ci", "ceux-là", "chacun", "chacune", "chaque", "cher",
           "chers", "chez", "chiche", "chut", "chère", "chères", "ci", "cinq",
           "cinquantaine", "cinquante", "cinquantième", "cinquième", "clac",
           "clic", "combien", "comme", "comment", "comparable", "comparables",
           "compris", "concernant", "contre", "couic", "crac", "d", "da",
           "dans", "de", "debout", "dedans", "dehors", "deja", "delà",
           "depuis", "dernier", "derniere", "derriere", "derrière", "des",
           "desormais", "desquelles", "desquels", "dessous", "dessus", "deux",
           "deuxième", "deuxièmement", "devant", "devers", "devra",
           "different", "differentes", "differents", "différent", "différente",
           "différentes", "différents", "dire", "directe", "directement",
           "dit", "dite", "dits", "divers", "diverse", "diverses", "dix",
           "dix-huit", "dix-neuf", "dix-sept", "dixième", "doit", "doivent",
           "donc", "dont", "douze", "douzième", "dring", "du", "duquel",
           "durant", "dès", "désormais", "e", "effet", "egale", "egalement",
           "egales", "eh", "elle", "elle-même", "elles", "elles-mêmes", "en",
           "encore", "enfin", "entre", "envers", "environ", "es", "est", "et",
           "etant", "etc", "etre", "eu", "euh", "eux", "eux-mêmes",
           "exactement", "excepté", "extenso", "exterieur", "f", "fais",
           "faisaient", "faisant", "fait", "façon", "feront", "fi", "flac",
           "floc", "font", "g", "gens", "h", "ha", "hein", "hem", "hep", "hi",
           "ho", "holà", "hop", "hormis", "hors", "hou", "houp", "hue", "hui",
           "huit", "huitième", "hum", "hurrah", "hé", "hélas", "i", "il",
           "ils", "importe", "j", "je", "jusqu", "jusque", "juste", "k", "l",
           "la", "laisser", "laquelle", "las", "le", "lequel", "les",
           "lesquelles", "lesquels", "leur", "leurs", "longtemps", "lors",
           "lorsque", "lui", "lui-meme", "lui-même", "là", "lès", "m", "ma",
           "maint", "maintenant", "mais", "malgre", "malgré", "maximale", "me",
           "meme", "memes", "merci", "mes", "mien", "mienne", "miennes",
           "miens", "mille", "mince", "minimale", "moi", "moi-meme",
           "moi-même", "moindres", "moins", "mon", "moyennant", "multiple",
           "multiples", "même", "mêmes", "n", "na", "naturel", "naturelle",
           "naturelles", "ne", "neanmoins", "necessaire", "necessairement",
           "neuf", "neuvième", "ni", "nombreuses", "nombreux", "non", "nos",
           "notamment", "notre", "nous", "nous-mêmes", "nouveau", "nul",
           "néanmoins", "nôtre", "nôtres", "o", "oh", "ohé", "ollé", "olé",
           "on", "ont", "onze", "onzième", "ore", "ou", "ouf", "ouias", "oust",
           "ouste", "outre", "ouvert", "ouverte", "ouverts", "o|", "où", "p",
           "paf", "pan", "par", "parce", "parfois", "parle", "parlent",
           "parler", "parmi", "parseme", "partant", "particulier",
           "particulière", "particulièrement", "pas", "passé", "pendant",
           "pense", "permet", "personne", "peu", "peut", "peuvent", "peux",
           "pff", "pfft", "pfut", "pif", "pire", "plein", "plouf", "plus",
           "plusieurs", "plutôt", "possessif", "possessifs", "possible",
           "possibles", "pouah", "pour", "pourquoi", "pourrais", "pourrait",
           "pouvait", "prealable", "precisement", "premier", "première",
           "premièrement", "pres", "probable", "probante", "procedant",
           "proche", "près", "psitt", "pu", "puis", "puisque", "pur", "pure",
           "q", "qu", "quand", "quant", "quant-à-soi", "quanta", "quarante",
           "quatorze", "quatre", "quatre-vingt", "quatrième", "quatrièmement",
           "que", "quel", "quelconque", "quelle", "quelles", "quelqu'un",
           "quelque", "quelques", "quels", "qui", "quiconque", "quinze",
           "quoi", "quoique", "r", "rare", "rarement", "rares", "relative",
           "relativement", "remarquable", "rend", "rendre", "restant", "reste",
           "restent", "restrictif", "retour", "revoici", "revoilà", "rien",
           "s", "sa", "sacrebleu", "sait", "sans", "sapristi", "sauf", "se",
           "sein", "seize", "selon", "semblable", "semblaient", "semble",
           "semblent", "sent", "sept", "septième", "sera", "seraient",
           "serait", "seront", "ses", "seul", "seule", "seulement", "si",
           "sien", "sienne", "siennes", "siens", "sinon", "six", "sixième",
           "soi", "soi-même", "soit", "soixante", "son", "sont", "sous",
           "souvent", "specifique", "specifiques", "speculatif", "stop",
           "strictement", "subtiles", "suffisant", "suffisante", "suffit",
           "suis", "suit", "suivant", "suivante", "suivantes", "suivants",
           "suivre", "superpose", "sur", "surtout", "t", "ta", "tac", "tant",
           "tardive", "te", "tel", "telle", "tellement", "telles", "tels",
           "tenant", "tend", "tenir", "tente", "tes", "tic", "tien", "tienne",
           "tiennes", "tiens", "toc", "toi", "toi-même", "ton", "touchant",
           "toujours", "tous", "tout", "toute", "toutefois", "toutes",
           "treize", "trente", "tres", "trois", "troisième", "troisièmement",
           "trop", "très", "tsoin", "tsouin", "tu", "té", "u", "un", "une",
           "unes", "uniformement", "unique", "uniques", "uns", "v", "va",
           "vais", "vas", "vers", "via", "vif", "vifs", "vingt", "vivat",
           "vive", "vives", "vlan", "voici", "voilà", "vont", "vos", "votre",
           "vous", "vous-mêmes", "vu", "vé", "vôtre", "vôtres", "w", "x", "y",
           "z", "zut", "à", "â", "ça", "ès", "étaient", "étais", "était",
           "étant", "été", "être", "ô"},
    "it": {"IE", "a", "abbastanza", "abbia", "abbiamo", "abbiano", "abbiate",
           "accidenti", "ad", "adesso", "affinche", "agl", "agli", "ahime",
           "ahimè", "ai", "al", "alcuna", "alcuni", "alcuno", "all", "alla",
           "alle", "allo", "allora", "altri", "altrimenti", "altro", "altrove",
           "altrui", "anche", "ancora", "anni", "anno", "ansa", "anticipo",
           "assai", "attesa", "attraverso", "avanti", "avemmo", "avendo",
           "avente", "aver", "avere", "averlo", "avesse", "avessero", "avessi",
           "avessimo", "aveste", "avesti", "avete", "aveva", "avevamo",
           "avevano", "avevate", "avevi", "avevo", "avrai", "avranno",
           "avrebbe", "avrebbero", "avrei", "avremmo", "avremo", "avreste",
           "avresti", "avrete", "avrà", "avrò", "avuta", "avute", "avuti",
           "avuto", "basta", "bene", "benissimo", "berlusconi", "brava",
           "bravo", "c", "casa", "caso", "cento", "certa", "certe", "certi",
           "certo", "che", "chi", "chicchessia", "chiunque", "ci", "ciascuna",
           "ciascuno", "cima", "cio", "cioe", "cioè", "circa", "citta",
           "città", "ciò", "co", "codesta", "codesti", "codesto", "cogli",
           "coi", "col", "colei", "coll", "coloro", "colui", "come", "cominci",
           "comunque", "con", "concernente", "conciliarsi", "conclusione",
           "consiglio", "contro", "cortesia", "cos", "cosa", "cosi", "così",
           "cui", "d", "da", "dagl", "dagli", "dai", "dal", "dall", "dalla",
           "dalle", "dallo", "dappertutto", "davanti", "degl", "degli", "dei",
           "del", "dell", "della", "delle", "dello", "dentro", "detto", "deve",
           "di", "dice", "dietro", "dire", "dirimpetto", "diventa",
           "diventare", "diventato", "dopo", "dov", "dove", "dovra", "dovrà",
           "dovunque", "due", "dunque", "durante", "e", "ebbe", "ebbero",
           "ebbi", "ecc", "ecco", "ed", "effettivamente", "egli", "ella",
           "entrambi", "eppure", "era", "erano", "eravamo", "eravate", "eri",
           "ero", "esempio", "esse", "essendo", "esser", "essere", "essi",
           "ex", "fa", "faccia", "facciamo", "facciano", "facciate", "faccio",
           "facemmo", "facendo", "facesse", "facessero", "facessi",
           "facessimo", "faceste", "facesti", "faceva", "facevamo", "facevano",
           "facevate", "facevi", "facevo", "fai", "fanno", "farai", "faranno",
           "fare", "farebbe", "farebbero", "farei", "faremmo", "faremo",
           "fareste", "faresti", "farete", "farà", "farò", "fatto", "favore",
           "fece", "fecero", "feci", "fin", "finalmente", "finche", "fine",
           "fino", "forse", "forza", "fosse", "fossero", "fossi", "fossimo",
           "foste", "fosti", "fra", "frattempo", "fu", "fui", "fummo", "fuori",
           "furono", "futuro", "generale", "gia", "giacche", "giorni",
           "giorno", "già", "gli", "gliela", "gliele", "glieli", "glielo",
           "gliene", "governo", "grande", "grazie", "gruppo", "ha", "haha",
           "hai", "hanno", "ho", "i", "ieri", "il", "improvviso", "in", "inc",
           "infatti", "inoltre", "insieme", "intanto", "intorno", "invece",
           "io", "l", "la", "lasciato", "lato", "lavoro", "le", "lei", "li",
           "lo", "lontano", "loro", "lui", "lungo", "luogo", "là", "ma",
           "macche", "magari", "maggior", "mai", "male", "malgrado",
           "malissimo", "mancanza", "marche", "me", "medesimo", "mediante",
           "meglio", "meno", "mentre", "mesi", "mezzo", "mi", "mia", "mie",
           "miei", "mila", "miliardi", "milioni", "minimi", "ministro", "mio",
           "modo", "molti", "moltissimo", "molto", "momento", "mondo", "mosto",
           "nazionale", "ne", "negl", "negli", "nei", "nel", "nell", "nella",
           "nelle", "nello", "nemmeno", "neppure", "nessun", "nessuna",
           "nessuno", "niente", "no", "noi", "non", "nondimeno", "nonostante",
           "nonsia", "nostra", "nostre", "nostri", "nostro", "novanta", "nove",
           "nulla", "nuovo", "o", "od", "oggi", "ogni", "ognuna", "ognuno",
           "oltre", "oppure", "ora", "ore", "osi", "ossia", "ottanta", "otto",
           "paese", "parecchi", "parecchie", "parecchio", "parte", "partendo",
           "peccato", "peggio", "per", "perche", "perchè", "perché", "percio",
           "perciò", "perfino", "pero", "persino", "persone", "però", "piedi",
           "pieno", "piglia", "piu", "piuttosto", "più", "po", "pochissimo",
           "poco", "poi", "poiche", "possa", "possedere", "posteriore",
           "posto", "potrebbe", "preferibilmente", "presa", "press", "prima",
           "primo", "principalmente", "probabilmente", "proprio", "puo",
           "pure", "purtroppo", "può", "qualche", "qualcosa", "qualcuna",
           "qualcuno", "quale", "quali", "qualunque", "quando", "quanta",
           "quante", "quanti", "quanto", "quantunque", "quasi", "quattro",
           "quel", "quella", "quelle", "quelli", "quello", "quest", "questa",
           "queste", "questi", "questo", "qui", "quindi", "realmente",
           "recente", "recentemente", "registrazione", "relativo", "riecco",
           "salvo", "sara", "sarai", "saranno", "sarebbe", "sarebbero",
           "sarei", "saremmo", "saremo", "sareste", "saresti", "sarete",
           "sarà", "sarò", "scola", "scopo", "scorso", "se", "secondo",
           "seguente", "seguito", "sei", "sembra", "sembrare", "sembrato",
           "sembri", "sempre", "senza", "sette", "si", "sia", "siamo", "siano",
           "siate", "siete", "sig", "solito", "solo", "soltanto", "sono",
           "sopra", "sotto", "spesso", "srl", "sta", "stai", "stando",
           "stanno", "starai", "staranno", "starebbe", "starebbero", "starei",
           "staremmo", "staremo", "stareste", "staresti", "starete", "starà",
           "starò", "stata", "state", "stati", "stato", "stava", "stavamo",
           "stavano", "stavate", "stavi", "stavo", "stemmo", "stessa",
           "stesse", "stessero", "stessi", "stessimo", "stesso", "steste",
           "stesti", "stette", "stettero", "stetti", "stia", "stiamo",
           "stiano", "stiate", "sto", "su", "sua", "subito", "successivamente",
           "successivo", "sue", "sugl", "sugli", "sui", "sul", "sull", "sulla",
           "sulle", "sullo", "suo", "suoi", "tale", "tali", "talvolta",
           "tanto", "te", "tempo", "ti", "titolo", "torino", "tra", "tranne",
           "tre", "trenta", "troppo", "trovato", "tu", "tua", "tue", "tuo",
           "tuoi", "tutta", "tuttavia", "tutte", "tutti", "tutto", "uguali",
           "ulteriore", "ultimo", "un", "una", "uno", "uomo", "va", "vale",
           "vari", "varia", "varie", "vario", "verso", "vi", "via", "vicino",
           "visto", "vita", "voi", "volta", "volte", "vostra", "vostre",
           "vostri", "vostro", "è"},
       "uk": set(uk_stopwrods.split("\n"))
}

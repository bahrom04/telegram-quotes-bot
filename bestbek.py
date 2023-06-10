from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes,ConversationHandler,MessageHandler,filters
from random import choice

uzbek_quotes = ["Dunyoda ko'rishni xohlagan o'zgarish bo'l. - Mahatma Gandi",
     "To'xtamaguningizcha qanchalik sekin borishingiz muhim emas. - Konfutsiy",
     "Tasavvur bilimdan muhimroqdir. Bilim cheklangan. Tasavvur dunyoni o'rab oladi. - Albert Eynshteyn",
     "Ishoning, qila olasiz va siz yarim yo'ldasiz. - Teodor Ruzvelt",
     "Buyuk ish qilishning yagona yo'li - qilayotgan ishingizni sevishdir. - Stiv Jobs",
     "Oxir-oqibat, biz dushmanlarimizning so'zlarini emas, balki do'stlarimizning sukutini eslaymiz. - Martin Lyuter King Jr.",
     "Men muvaffaqiyatsizlikka uchramadim. Men ishlamaydigan 10 000 ta usulni topdim. - Tomas Edison",
     "Muvaffaqiyat yakuniy emas, muvaffaqiyatsizlik halokatli emas: davom etish uchun jasorat muhimdir. - Uinston Cherchill",
     "Hayot 10% biz bilan nima sodir bo'lishidan va 90% biz bunga qanday munosabatda bo'lishimizdan iborat. - Charlz R. Svindoll",
     "Biz o'ylagan narsamizga aylanamiz. - Erl Nightingale",
     "Yomonlikning g'alabasi uchun zarur bo'lgan yagona narsa - bu yaxshi odamlar hech narsa qilmaslikdir. - Edmund Burk",
     "Biz qayta-qayta qiladigan narsamiz. Demak, mukammallik - bu harakat emas, balki odat. - Aristotel",
     "Kelajakni bashorat qilishning eng yaxshi usuli uni ixtiro qilishdir. - Alan Kay",
     "Baxt bu tayyor narsa emas. Bu sizning harakatlaringizdan kelib chiqadi. - Dalay Lama",
     "Hammasini sev, bir nechtasiga ishon, hech kimga yomonlik qil. - Uilyam Shekspir"
     "Yashashdagi eng katta shon-sharaf hech qachon yiqilmasligimizda emas, balki har yiqilganimizda ko'tarilishimizdadir. - Nelson Mandela"
     "O'zing bo'l; hamma allaqachon olingan. - Oskar Uayld",
     "Muvaffaqiyatli odam bo'lishga emas, balki qadrli odam bo'lishga harakat qiling. - Albert Eynshteyn",
     "Biz dunyoda ko'rishni istagan o'zgarish bo'lishimiz kerak. - Mahatma Gandi",
     "Biz hammaga yordam bera olmaymiz, lekin hamma kimgadir yordam berishi mumkin. - Ronald Reygan",
     "Agar siz baxtli hayot kechirishni istasangiz, uni odamlarga yoki narsalarga emas, balki maqsadga bog'lang. - Albert Eynshteyn",
     "Siz suratga olmagan suratlarning 100 foizini o'tkazib yuborasiz. - Ueyn Gretzki",
     "Men muvaffaqiyatimni shu bilan bog'layman: men hech qachon uzr bermaganman yoki bahona ham qilmaganman. - Florens Nightingale",
     "Men zerikishdan ko'ra ehtirosdan o'lganni afzal ko'raman. - Vinsent van Gog",
     "Taqdirimiz yulduzlarda emas, balki o'zimizda. - Uilyam Shekspir"
     "Mening orzuim bir kun kelib, bu xalq bosh ko'tarib, o'z e'tiqodining asl ma'nosini hayotga tatbiq etsa: “Biz bu haqiqatlarni o'z-o'zidan ravshan deb bilamiz, barcha insonlar teng yaratilgan”. - Martin Lyuter King Jr.",
     "Muvaffaqiyatsizlik - bu variant emas. Hamma muvaffaqiyatga erishishi kerak. - Arnold Shvartsenegger",
     "Eng yaxshi qasos - bu katta muvaffaqiyat. - Frenk Sinatra",
     "Men ishonamanki, agar inson doimo osmonga qarasa, qanotli bo'ladi. - Gustav Flober",
     "Biz qo'rqishimiz kerak bo'lgan yagona narsa - qo'rquvning o'zi. - Franklin D. Ruzvelt",
     "Mantiq sizni A dan B gacha olib boradi. Tasavvur sizni hamma joyga olib boradi. - Albert Eynshteyn",
     "Tinchlik tabassumdan boshlanadi. - Tereza ona",
     "Kechagi kun bugunning ko'p qismini egallashiga yo'l qo'ymang. - Uill Rojers",
     "O'zingiz uchrashmoqchi bo'lgan odam turi bo'ling. - Noma'lum",
     "Agar siz boshqa odamlarga xohlagan narsalarini olishiga yordam bersangiz, hayotda siz xohlagan hamma narsaga ega bo'lishingiz mumkin. - Zig Ziglar",
     "Ertangi kunimizni anglashimizning yagona chegarasi bugungi kundagi shubhalarimiz bo'ladi. - Franklin D. Ruzvelt",
     "Aql - bu hamma narsa. O'zingni o'ylagan narsang. - Budda",
     "Biz o'ylagan narsamiz. Biz nima bo'lsak, hamma narsa bizning fikrlarimiz bilan paydo bo'ladi. Bizning fikrlarimiz bilan biz dunyoni yaratamiz. - Budda",
     "Eng qorong'u daqiqalarimizda biz yorug'likni ko'rishga e'tibor qaratishimiz kerak. - Aristotel Onassis",
     "Sizning hozirgi sharoitingiz qaerga borishingizni aniqlamaydi; ular faqat qaerdan boshlashingizni belgilaydi. - Nido Qubein",
     "Hamma narsaning go'zalligi bor, lekin uni hamma ham ko'ravermaydi. - Konfutsiy",
     "Agar rostini aytsangiz, hech narsani eslab qolishingiz shart emas. - Mark Tven",
     "Qo'lingdan kelmaydigan narsa qila oladigan narsangizga xalaqit berishiga yo'l qo'ymang. - Jon Vuden",
     "Muvaffaqiyat ishtiyoqni yo'qotmasdan muvaffaqiyatsizlikdan muvaffaqiyatsizlikka o'tishdan iborat. - Uinston Cherchill",
     "Sizni doimo boshqa narsaga aylantirmoqchi bo'lgan dunyoda o'zingiz bo'lish - bu eng katta yutuq. - Ralf Valdo Emerson",
     "Shamol yo'nalishini o'zgartira olmaysiz, ammo yelkaningizni har doim manzilingizga etib borish uchun sozlashingiz mumkin. - Jimmi Din",
     "Agar siz biror narsa uchun turmasangiz, hamma narsaga tushib qolasiz. - Malkolm X",
     "O'rganilmagan hayot yashashga arzimaydi. - Sokrat",
     "Muvaffaqiyatsiz bo'lish qiyin, lekin hech qachon muvaffaqiyatga erishmaslik bundan ham yomoni. - Teodor Ruzvelt",
     "Yashashdagi eng katta shon-shuhrat hech qachon yiqilmasligimizda emas, balki har yiqilganimizda ko'tarilishdadir. - Ralf Valdo Emerson"
     "Men hayot haqida o'rganganlarimni uchta so'z bilan ifodalashim mumkin: u davom etmoqda. - Robert Frost",
     "Muvaffaqiyat baxtning kaliti emas. Baxt - muvaffaqiyat kaliti. Agar qilayotgan ishingizni sevsangiz, muvaffaqiyatga erishasiz. - Albert Shvaytser",
     "Men hayotimda qayta-qayta muvaffaqiyatsizlikka uchraganman va shuning uchun ham muvaffaqiyatga erishdim. - Maykl Jordan",
     "Biz chekli umidsizlikni qabul qilishimiz kerak, lekin hech qachon cheksiz umidni yo'qotmaslik kerak. - Martin Lyuter King Jr.",
     "Qaerga borsangiz ham muhabbatni yoying. Hech kim sizning oldingizga baxtliroq kelmasin. - Tereza ona",
     "O'tmishda o'ylamang, kelajakni orzu qilmang, ongingizni hozirgi daqiqaga qarating. - Budda",
     "Yuzingizni har doim quyosh nuri tomon yo'naltiring - va sizning orqangizdan soyalar tushadi. - Uolt Uitman",
     "Siz boshqa maqsadni qo'yish yoki yangi orzuni orzu qilish uchun hech qachon keksa emassiz. - C. S. Lyuis",
     "Biz nima deb o'ylaymiz, biz bo'lamiz. - Budda",
     "O'zingizga va bor narsangizga ishoning. Bilingki, ichingizda har qanday to'siqdan ham kattaroq narsa bor. - Kristian D. Larson",
     "Men sharoitim mahsuli emasman. Men qarorlarim mahsuliman. - Stiven Kovi",
     "Yagona haqiqiy donolik hech narsa bilmasligingizni bilishdir. - Sokrat"
     "Vaqtingiz cheklangan, uni boshqa birovning hayotiga sarflamang. - Stiv Jobs",
     "Hayot bir qator tabiiy va o'z-o'zidan paydo bo'ladigan o'zgarishlardir. Ularga qarshilik qilmang - bu faqat qayg'u keltiradi. Haqiqat haqiqat bo'lsin. Ishlar tabiiy ravishda o'zlari xohlagan tarzda oldinga o'tsin. - Lao Tzu",
     "Yaxshi fikrga ega bo'lishning yagona yo'li - ko'p g'oyalarga ega bo'lishdir. - Linus Pauling",
     "Muvaffaqiyatli bo'lishga emas, balki qadrli bo'lishga intiling. - Albert Eynshteyn",
     "Agar siz orzularingizni ro'yobga chiqarishni istasangiz, birinchi navbatda uyg'onishingiz kerak. - J. M. Pauer",
     "Har bir kunni yig'ib olgan hosilingiz bilan emas, balki ekkan urug'ingiz bilan baholang. - Robert Lui Stivenson"
     "Biz ko'p mag'lubiyatlarga duch kelishimiz mumkin, ammo biz mag'lub bo'lmasligimiz kerak. - Maya Anjelu",
     "Dunyoda ko'rishni xohlagan o'zgarish bo'l. - Mahatma Gandi",
     "Amal qiladigan ozgina bilim, behuda bilimdan cheksiz qimmatroqdir. - Xalil Gibran",
     "Ikki narsa cheksizdir: koinot va inson ahmoqligi; va men koinot haqida ishonchim komil emas. - Albert Eynshteyn",
     "Optimizm - bu muvaffaqiyatga olib keladigan ishonch. Umid va ishonchsiz hech narsa qilib bo'lmaydi. - Helen Keller",
     "Bizning barcha orzularimiz amalga oshishi mumkin, agar ularga erishish uchun jasoratimiz bo'lsa. - Uolt Disney",
     "Hayot o'zingni topishdan iborat emas, hayot o'zingni yaratishdan iborat. - Jorj Bernard Shou"
     "Bu har doim amalga oshmaguncha imkonsiz bo'lib tuyuladi. - Nelson Mandela",
     "Jasorat har doim ham bo'kmaydi. Ba'zida jasorat kun oxirida ertaga yana urinib ko'raman degan sokin ovozdir. - Meri Enn Radmacher",
     "Siz va maqsadingiz o'rtasida turgan yagona narsa bu nima uchun bunga erisha olmasligingiz haqida o'zingizga gapiradigan bema'ni hikoyadir. - Jordan Belfort",
     "Buyuklikdan qo'rqmang. Ba'zilar buyuk bo'lib tug'iladilar, ba'zilari buyuklikka erishadilar, boshqalari esa ulug'vorlikka intilishadi. - Uilyam Shekspir",
     "Inson faqat o'z fikrlarining mahsuli. U nima o'ylasa, u bo'ladi. - Mahatma Gandi",
     ]
quote = [
    "Be the change you wish to see in the world. - Mahatma Gandhi",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "Imagination is more important than knowledge. Knowledge is limited. Imagination encircles the world. - Albert Einstein",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "In the end, we will remember not the words of our enemies, but the silence of our friends. - Martin Luther King Jr.",
    "I have not failed. I've just found 10,000 ways that won't work. - Thomas Edison",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
    "Life is 10% what happens to us and 90 percent how we react to it. - Charles R. Swindoll",
    "We become what we think about. - Earl Nightingale",
    "The only thing necessary for the triumph of evil is for good men to do nothing. - Edmund Burke",
    "We are what we repeatedly do. Excellence, then, is not an act, but a habit. - Aristotle",
    "The best way to predict the future is to invent it. - Alan Kay",
    "Happiness is not something ready made. It comes from your own actions. - Dalai Lama",
    "Love all, trust a few, do wrong to none. - William Shakespeare",
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
    "Be yourself; everyone else is already taken. - Oscar Wilde",
    "Try not to become a man of success, but rather try to become a man of value. - Albert Einstein",
    "We must be the change we wish to see in the world. - Mahatma Gandhi",
    "We can't help everyone, but everyone can help someone. - Ronald Reagan",
    "If you want to live a happy life, tie it to a goal, not to people or things. - Albert Einstein",
    "You miss 100 percent of the shots you don't take. - Wayne Gretzky",
    "I attribute my success to this: I never gave or took any excuse. - Florence Nightingale",
    "I would rather die of passion than of boredom. - Vincent van Gogh",
    "It is not in the stars to hold our destiny but in ourselves. - William Shakespeare",
    "I have a dream that one day this nation will rise up and live out the true meaning of its creed: 'We hold these truths to be self-evident, that all men are created equal.' - Martin Luther King Jr.",
    "Failure is not an option. Everyone has to succeed. - Arnold Schwarzenegger",
    "The best revenge is massive success. - Frank Sinatra",
    "I believe that if one always looks at the skies, one will end up with wings. - Gustave Flaubert",
    "The only thing we have to fear is fear itself. - Franklin D. Roosevelt",
    "Logic will get you from A to B. Imagination will take you everywhere. - Albert Einstein",
    "Peace begins with a smile. - Mother Teresa",
    "Don't let yesterday take up too much of today. - Will Rogers",
    "Be the type of person you want to meet. - Unknown",
    "You can have everything in life you want, if you will just help enough other people get what they want. - Zig Ziglar",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "The mind is everything. What you think you become. - Buddha",
    "We are what we think. All that we are arises with our thoughts. With our thoughts, we make the world. - Buddha",
    "It is during our darkest moments that we must focus to see the light. - Aristotle Onassis",
    "Your present circumstances don't determine where you can go; they merely determine where you start. - Nido Qubein",
    "Everything has beauty, but not everyone sees it. - Confucius",
    "If you tell the truth, you don't have to remember anything. - Mark Twain",
    "Don't let what you cannot do interfere with what you can do. - John Wooden",
    "Success consists of going from failure to failure without loss of enthusiasm. - Winston Churchill",
    "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment. - Ralph Waldo Emerson",
    "You can't change the direction of the wind, but you can adjust your sails to always reach your destination. - Jimmy Dean",
    "If you don't stand for something, you will fall for anything. - Malcolm X",
    "The unexamined life is not worth living. - Socrates",
    "It is hard to fail, but it is worse never to have tried to succeed. - Theodore Roosevelt",
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Ralph Waldo Emerson",
    "In three words I can sum up everything I've learned about life: it goes on. - Robert Frost",
    "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful. - Albert Schweitzer",
    "I've failed over and over and over again in my life and that is why I succeed. - Michael Jordan",
    "We must accept finite disappointment, but never lose infinite hope. - Martin Luther King Jr.",
    "Spread love everywhere you go. Let no one ever come to you without leaving happier. - Mother Teresa",
    "Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment. - Buddha",
    "Keep your face always toward the sunshine - and shadows will fall behind you. - Walt Whitman",
    "You are never too old to set another goal or to dream a new dream. - C. S. Lewis",
    "What we think, we become. - Buddha",
    "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. - Christian D. Larson",
    "I am not a product of my circumstances. I am a product of my decisions. - Stephen Covey",
    "The only true wisdom is in knowing you know nothing. - Socrates",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
    "Life is a series of natural and spontaneous changes. Don't resist them - that only creates sorrow. Let reality be reality. Let things flow naturally forward in whatever way they like. - Lao Tzu",
    "The only way to have a good idea is to have a lot of ideas. - Linus Pauling",
    "Strive not to be a success, but rather to be of value. - Albert Einstein",
    "If you want to make your dreams come true, the first thing you have to do is wake up. - J. M. Power",
    "Don't judge each day by the harvest you reap but by the seeds that you plant. - Robert Louis Stevenson",
    "We may encounter many defeats but we must not be defeated. - Maya Angelou",
    "Be the change that you wish to see in the world. - Mahatma Gandhi",
    "A little knowledge that acts is worth infinitely more than much knowledge that is idle. - Kahlil Gibran",
    "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe. - Albert Einstein",
    "Optimism is the faith that leads to achievement. Nothing can be done without hope and confidence. - Helen Keller",
    "All our dreams can come true, if we have the courage to pursue them. - Walt Disney",
    "Life isn't about finding yourself. Life is about creating yourself. - George Bernard Shaw",
    "It always seems impossible until it's done. - Nelson Mandela",
    "Courage doesn't always roar. Sometimes courage is the quiet voice at the end of the day saying 'I will try again tomorrow.' - Mary Anne Radmacher",
    "The only thing standing between you and your goal is the bullshit story you keep telling yourself as to why you can't achieve it. - Jordan Belfort",
    "Be not afraid of greatness. Some are born great, some achieve greatness, and others have greatness thrust upon them. - William Shakespeare",
    "A man is but the product of his thoughts. What he thinks, he becomes. - Mahatma Gandhi",
]

buttons = ReplyKeyboardMarkup([['Uzbek'],['English']],resize_keyboard=True)

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        f"Assalomu alaykum {update.effective_user.first_name}\nEng mashxur iqiboslarini o'qish uchun tilni tanlang",reply_markup=buttons)
    return 1

async def uzbek(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(choice(uzbek_quotes))

async def english(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(choice(quote))
    



app = ApplicationBuilder().token("YOUR_TOKEN").build()

conversation_handler = ConversationHandler(
    entry_points = [CommandHandler('hello',hello)],
    states= {
        1:[
            MessageHandler(filters.Regex('^(Uzbek)$'),uzbek),
            MessageHandler(filters.Regex('^(English)$'),english)
        ]
    },
    fallbacks=[MessageHandler(filters.TEXT,hello)]
)
app.add_handler(conversation_handler)

app.run_polling()

ИНСТРУКЦИЯ:

Скопируйте папку East-Showdown и East-Showdown.mod из архива в Документы\Paradox Interactive\Hearts of Iron IV\mod

Если у вас при запуске мода запускается обычная игра, то дело скорее всего в адресе до мода:
1) Откройте East-Showdown.mod 
2) Найдите строку которая выглядит примерно как path="C:/Users/Мобик-ДНР/Documents/Paradox Interactive/Hearts of Iron IV/mod/East-Showdown". Если в этой строке вы обнаружили кириллицу, то необходимо поменять адрес мода
3) Перенесите папку мода (Важно! Без файла East-Showdown.mod) в то место докуда в адресной строке не будет кириллицы. Пример: D:\East-Showdown
4) Скопируйте и вставьте адрес мода в строчку path="***" заместо старого адреса. Замените все \ на / (Очень важно. Без этого не заработает). У вас должно получится что-то вроде path="D:/East-Showdown"
5) Пробуйте запускать. Если не получается то вы можете обратиться к администраторам группы ВК, или же нашему сообществу в Discord



ДЛЯ РАЗРАБОТЧИКОВ (Git):

Если вы клонируете репозиторий через Git, необходимо инициализировать submodule для инструмента локализации:

git clone --recurse-submodules https://github.com/East-Showdown/East-Showdown.git

Или если уже склонировали:

git submodule update --init --recursive



FOR DEVELOPERS (Git):

If you're cloning the repository via Git, you need to initialize the submodule for the localization tool:

git clone --recurse-submodules https://github.com/East-Showdown/East-Showdown.git

Or if already cloned:

git submodule update --init --recursive



GUIDE:

Copy the folder East-Showdown and East-Showdown.mod from the archive to Documents\Paradox Interactive\Hearts of Iron IV\mod
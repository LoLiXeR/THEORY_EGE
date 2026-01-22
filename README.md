# THEORY_EGE
Все задания в Readme - задания эксель, ибо в код их не встроить

## Задание 18
### Само задание
<img width="1179" height="345" alt="task18" src="https://github.com/user-attachments/assets/f878f930-3d82-4b7b-a244-65ae69ec85c0" />
Смотрим старт (левый верхний угол)
Для начала смотрим как ходит (вправо и вниз)
Смотрим заряд или монета (монета), поскольку при заряде мы тратим энергию, а при монетах собираем
Смотрим ограничения (ограниченые справа и снизу стенами)
<br><br><br><br>
<img width="1920" height="1032" alt="task18solution (1)" src="https://github.com/user-attachments/assets/54070d0b-b8dc-4c5d-b1fb-3d4d0dc5cf81" />
Открываем задание, выделяем и копируем данную нам таблицу с числами через Ctrl+C
<br>
<img width="1920" height="1032" alt="task18solution (2)" src="https://github.com/user-attachments/assets/f13a9f87-0f15-4fb9-9475-b24db011bbe3" />
Вставляем таблицу чуть ниже прямо под изначальной таблицей
Нажимаем ПКМ, очистить содержимое
<br>
<img width="1920" height="1032" alt="task18solution (3)" src="https://github.com/user-attachments/assets/ccf3fb3c-7867-4df2-a5ac-2f80f0e8d0ce" />
У нас появляется пустая таблица только с форматами, она нам и нужна
<br>
<img width="1920" height="1032" alt="task18solution (4)" src="https://github.com/user-attachments/assets/0656ef12-0fd0-4f50-bf30-59f4dfe35cfd" />
Вписываем в начальную позицию нашего робота число соответствующее позиции A1 (левый верхний угол)
<br>
<img width="1920" height="1032" alt="task18solution (5)" src="https://github.com/user-attachments/assets/c8ddc50d-d3a1-42cc-b6f4-e32abac233eb" />
Начинаем движение, вписываем в ячейку справа формулу прибавляющую к позиции A23 позицию B1 (сдвинулись вправо и собрали монетку)
<br>
<img width="1920" height="1032" alt="task18solution (7)" src="https://github.com/user-attachments/assets/a913cc87-ce5e-4aec-80bd-a493f0e829fc" />
Продлеваем до конца, жмём заполнить только значения
<br>
<img width="1920" height="1032" alt="task18solution (8)" src="https://github.com/user-attachments/assets/8445f068-435d-4d78-b9e7-a7201005fb22" />
Повторяем предыдущие действия для левой колонки, затем начинаем движение по площади, вписывая формулу считающую максимальную сумму между переходом от ячеек A24 и B23
<br>
<img width="1920" height="1032" alt="task18solution (9)" src="https://github.com/user-attachments/assets/78709d34-76f9-46c8-923a-a7f5c8534dbb" />
<img width="1920" height="1032" alt="task18solution (10)" src="https://github.com/user-attachments/assets/0fce8448-f131-42db-a5e8-80bf0b07bbd6" />
<img width="1920" height="1032" alt="task18solution (11)" src="https://github.com/user-attachments/assets/03c72e61-b898-4b80-bb6f-fa019f4bebab" />
Продлеваем по всей таблице не забывая про нажатие заполнить только значения
<br>
<img width="1920" height="1032" alt="task18solution (12)" src="https://github.com/user-attachments/assets/3c898050-77cf-4e8a-8215-817f0bbce021" />
<img width="1920" height="1032" alt="task18solution (13)" src="https://github.com/user-attachments/assets/3083a5ac-bff0-4777-a736-8c6c07737547" />
<img width="1920" height="1032" alt="task18solution (14)" src="https://github.com/user-attachments/assets/47f00326-4999-4cc2-ac41-b9a15711c276" />
Регулируем движение около стенок (через них мы ходить не можем), а также у нас есть пустое поле, куда мы зайти не можем (если не отрегулировать движение возле этого поля, то позже у нас сломается расчёт минимума)
<br>
<img width="1920" height="1032" alt="task18solution (15)" src="https://github.com/user-attachments/assets/b71123b2-2c2a-4a65-875d-bc08bd4e5f22" />
Выделяем наши конечные точки чтобы было понятно куда смотреть
Смотрим максимальную сумму (обычно правый нижний угол, но бывают и приколы)
<br>
<img width="1920" height="1032" alt="task18solution (16)" src="https://github.com/user-attachments/assets/4e6fe239-110a-44e6-a448-397bfb45275a" />
Нажимаем Ctrl+F и заменяем Макс на Мин для расчёта минимальной суммы
<br>
<img width="1920" height="1032" alt="task18solution (17)" src="https://github.com/user-attachments/assets/27ec94da-67e5-49b0-be28-2e525d81c5d7" />
У нас есть ответ: 2628 839


## Задания 19, 20 и 21
### Само задание
<img width="1170" height="490" alt="task192021" src="https://github.com/user-attachments/assets/e9c90741-dddc-4717-8fd5-b3a7b0bf85d9" />
Здесь нас интересуют только 4 вещи:
1. Сколько куч? (Одна куча)
2. Какие ходы? (+2, +4, *2)
3. Когда выгрываем? (Кол-во камней >= 125)
4. За кого играем? (За победителя: в 19 за Ваню, в 20 за Петю, в 21 снова за Ваню)
<br>
<img width="1920" height="1032" alt="task192021solution (1)" src="https://github.com/user-attachments/assets/3dc8a4d9-5f85-452e-ae9f-f0e023f26a31" />
Создаём пустую таблицу
<br>
### Задание 19
<img width="1920" height="1032" alt="task192021solution (2)" src="https://github.com/user-attachments/assets/751bb116-dd19-4a8c-a836-0b5bfc687da6" />
Прописываем ячейки Куча, Проигравший, Победитель
<br>
<img width="1920" height="1032" alt="task192021solution (3)" src="https://github.com/user-attachments/assets/cae21330-4a1b-44b8-9678-49ad319cef24" />
Прописываем ходы (+2, +4, *2)
<br>
<img width="1920" height="1032" alt="task192021solution (4)" src="https://github.com/user-attachments/assets/900de9bd-98ad-4394-8115-2dbec9cbf50b" />
Прописываем ходы для Вани и продлеваем

<img width="1920" height="1032" alt="task192021solution (6)" src="https://github.com/user-attachments/assets/987898c7-bf2a-405b-bdb5-fbc5381a8877" />
<img width="1920" height="1032" alt="task192021solution (7)" src="https://github.com/user-attachments/assets/cc515dac-a420-487e-811f-41607b0f5056" />
<img width="1920" height="1032" alt="task192021solution (8)" src="https://github.com/user-attachments/assets/6cce7f20-244c-4024-8480-bba42f5b0754" />
Далее для нашего удобства создаём правила, которые будут подсвечивать числа >=125
<br>
<img width="1920" height="1032" alt="task192021solution (9)" src="https://github.com/user-attachments/assets/fb31e202-cc20-468d-80a2-01bb4694e2aa" />
Также мы можем всё выровнять чтобы всё было по красоте, и начинаем перебирать числа до тех пор, пока Ваня не будет зелёным во всех 3х ячейках (по условию при любом ходе Пети)
<br>
### Задание 20
<img width="1920" height="1032" alt="task192021solution (10)" src="https://github.com/user-attachments/assets/dfc1ff42-cc06-483e-91a3-3ce7f01a7432" />
Копируем кучу
<br>
<img width="1920" height="1032" alt="task192021solution (11)" src="https://github.com/user-attachments/assets/29e665ca-4884-4675-ab0d-66f2d08283cc" />
Копируем кучу, Петю и Ваню
<br>
<img width="1920" height="1032" alt="task192021solution (12)" src="https://github.com/user-attachments/assets/3be54707-ed6f-4bd0-a31f-5b0fb800282f" />
Создаём границы чтобы не запутаться
<br>
<img width="1920" height="1032" alt="task192021solution (13)" src="https://github.com/user-attachments/assets/b1103805-2dd0-4d69-b029-75ea49ae5ba5" />
Копируем и продлеваем
<br>
<img width="1920" height="1032" alt="task192021solution (14)" src="https://github.com/user-attachments/assets/bb2f54d4-fa2c-4742-b23d-556472f5fb42" />
Меняем кучу на Петю, Петю на Ваню, а ваню на Петю (чередование)
<br>
<img width="1920" height="1032" alt="task192021solution (15)" src="https://github.com/user-attachments/assets/6dce984e-e105-4878-b4c7-4c56f1a437e6" />
<img width="1920" height="1032" alt="task192021solution (16)" src="https://github.com/user-attachments/assets/0d9998d9-cc8d-4cb5-8574-f870aafd9909" />
Роллим до тех пор, пока не будет выполнено условие задачи

### Задание 21
<img width="1920" height="1032" alt="task192021solution (17)" src="https://github.com/user-attachments/assets/e52b0a3a-f4cf-4306-8f47-2586fa35e28a" />
<img width="1920" height="1032" alt="task192021solution (18)" src="https://github.com/user-attachments/assets/4dda802d-110c-4163-a391-62fc7906e891" />
<img width="1920" height="1032" alt="task192021solution (19)" src="https://github.com/user-attachments/assets/478bb405-b6c8-42ef-890d-e9e64246239a" />
<img width="1920" height="1032" alt="task192021solution (20)" src="https://github.com/user-attachments/assets/88c13d37-9d5a-4e8e-83c7-0e3796eeba30" />
Повторяем все предыдущие действия
Условия 
- у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при любой игре Пети;
- у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом.
Означают что Ваня не может выигрывать всегда 1м ходом, но 2м может всегда (самое главное чтобы не было 3х выиграных 1м ходом, 1-2 можно)

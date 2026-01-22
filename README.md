# THEORY_EGE
Все задания в Readme - задания эксель, ибо в код их не встроить

## Задание 18
### Само задание
<img width="1179" height="345" alt="task18" src="https://github.com/user-attachments/assets/f878f930-3d82-4b7b-a244-65ae69ec85c0" />
Смотрим старт (левый верхний угол)
Для начала смотрим как ходит (вправо и вниз)
Смотрим заряд или монета (монета), поскольку при заряде мы тратим энергию, а при монетах собираем
Смотрим ограничения (ограниченые справа и снизу стенами)
<img width="1920" height="1032" alt="task18solution (1)" src="https://github.com/user-attachments/assets/54070d0b-b8dc-4c5d-b1fb-3d4d0dc5cf81" />
Открываем задание, выделяем и копируем данную нам таблицу с числами через Ctrl+C
<img width="1920" height="1032" alt="task18solution (2)" src="https://github.com/user-attachments/assets/f13a9f87-0f15-4fb9-9475-b24db011bbe3" />
Вставляем таблицу чуть ниже прямо под изначальной таблицей
Нажимаем ПКМ, очистить содержимое
<img width="1920" height="1032" alt="task18solution (3)" src="https://github.com/user-attachments/assets/ccf3fb3c-7867-4df2-a5ac-2f80f0e8d0ce" />
У нас появляется пустая таблица только с форматами, она нам и нужна
<img width="1920" height="1032" alt="task18solution (4)" src="https://github.com/user-attachments/assets/0656ef12-0fd0-4f50-bf30-59f4dfe35cfd" />
Вписываем в начальную позицию нашего робота число соответствующее позиции A1 (левый верхний угол)
<img width="1920" height="1032" alt="task18solution (5)" src="https://github.com/user-attachments/assets/c8ddc50d-d3a1-42cc-b6f4-e32abac233eb" />
Начинаем движение, вписываем в ячейку справа формулу прибавляющую к позиции A23 позицию B1 (сдвинулись вправо и собрали монетку)
<img width="1920" height="1032" alt="task18solution (7)" src="https://github.com/user-attachments/assets/a913cc87-ce5e-4aec-80bd-a493f0e829fc" />
Продлеваем до конца, жмём заполнить только значения
<img width="1920" height="1032" alt="task18solution (8)" src="https://github.com/user-attachments/assets/8445f068-435d-4d78-b9e7-a7201005fb22" />
Повторяем предыдущие действия для левой колонки, затем начинаем движение по площади, вписывая формулу считающую максимальную сумму между переходом от ячеек A24 и B23
<img width="1920" height="1032" alt="task18solution (9)" src="https://github.com/user-attachments/assets/78709d34-76f9-46c8-923a-a7f5c8534dbb" />
<img width="1920" height="1032" alt="task18solution (10)" src="https://github.com/user-attachments/assets/0fce8448-f131-42db-a5e8-80bf0b07bbd6" />
<img width="1920" height="1032" alt="task18solution (11)" src="https://github.com/user-attachments/assets/03c72e61-b898-4b80-bb6f-fa019f4bebab" />
Продлеваем по всей таблице не забывая про нажатие заполнить только значения
<img width="1920" height="1032" alt="task18solution (12)" src="https://github.com/user-attachments/assets/3c898050-77cf-4e8a-8215-817f0bbce021" />
<img width="1920" height="1032" alt="task18solution (13)" src="https://github.com/user-attachments/assets/3083a5ac-bff0-4777-a736-8c6c07737547" />
<img width="1920" height="1032" alt="task18solution (14)" src="https://github.com/user-attachments/assets/47f00326-4999-4cc2-ac41-b9a15711c276" />
Регулируем движение около стенок (через них мы ходить не можем), а также у нас есть пустое поле, куда мы зайти не можем (если не отрегулировать движение возле этого поля, то позже у нас сломается расчёт минимума)
<img width="1920" height="1032" alt="task18solution (15)" src="https://github.com/user-attachments/assets/b71123b2-2c2a-4a65-875d-bc08bd4e5f22" />
Выделяем наши конечные точки чтобы было понятно куда смотреть
Смотрим максимальную сумму (обычно правый нижний угол, но бывают и приколы)
<img width="1920" height="1032" alt="task18solution (16)" src="https://github.com/user-attachments/assets/4e6fe239-110a-44e6-a448-397bfb45275a" />
Нажимаем Ctrl+F и заменяем Макс на Мин для расчёта минимальной суммы
<img width="1920" height="1032" alt="task18solution (17)" src="https://github.com/user-attachments/assets/27ec94da-67e5-49b0-be28-2e525d81c5d7" />
У нас есть ответ: 2628 839


import sqlite3

connect = sqlite3.connect('homework_6.db')
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS homework_6(
        task_id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT,
        status TEXT,
        date DATE
);
""")

def register():
    description = input("Введите описание задач: ")
    status = input("Введите статус задач: ")
    date = input("Введите дату создания задач (YYYY-MM-DD): ")  # Изменил формат ввода

    cursor.execute("""
        INSERT INTO homework_6 (description, status, date)
        VALUES (?, ?, ?)
    """, (description, status, date))

    connect.commit()

# register()

def add_task(description, status='выполняется'):
    cursor.execute('INSERT INTO homework_6 (description, status) VALUES (?, ?)', (description, status))
    connect.commit()

def update_task_status(new_status, task_id):
    cursor.execute('''
    UPDATE homework_6
    SET status = ?
    WHERE task_id = ?
    ''', (new_status, task_id))
    connect.commit()

def delete_task(task_id):
    cursor.execute('DELETE FROM homework_6 WHERE task_id = ?', (task_id,))
    connect.commit()

def view_homework_6(date):
    cursor.execute('SELECT * FROM homework_6 WHERE date = ?', (date,))
    return cursor.fetchall()

# add_task('Первая задача')
# add_task('Вторая задача')
update_task_status('выполняется', 1) 
print(view_homework_6('2024-10-12'))
# delete_task(2)

# connect.close()

def select_finish():
    check_status = input('Введите статус задачи:')
    cursor.execute('''SELECT description, status, date from homework_6 WHERE status = ?''',(check_status,))
    vyvod = cursor.fetchall()
    for vyvods in vyvod:
        print(f'вот все решенные задачи {vyvod}')

select_finish()
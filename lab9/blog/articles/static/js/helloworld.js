// Список студентов (массив объектов)
const groupmates = [
    { name: 'Иван', surname: 'Умнов', group: 'БСТ-2201' },
    { name: 'Пётр', surname: 'Пернатый', group: 'БСТ-201' },
    { name: 'Анна', surname: 'Аннотация', group: 'БСТ-2202' },
    { name: 'Мария', surname: 'Маринад', group: 'БСТ-2203' },
    { name: 'Дмитрий', surname: 'Дмитриев', group: 'БСТ-2202' }
];

// Функция форматированного вывода студентов
function printStudents(students) {
    console.log('=== Список студентов ===');
    students.forEach((student, index) => {
        console.log(`${index + 1}. ${student.surname} ${student.name} - Группа: ${student.group}`);
    });
    console.log(`Всего студентов: ${students.length}`);
    console.log('========================');
}

// Вызов функции для проверки
printStudents(groupmates);

// Функция фильтрации студентов по группе
function filterByGroup(students, groupName) {
    const filtered = students.filter(student => student.group === groupName);
    console.log(`\n=== Студенты группы ${groupName} ===`);
    if (filtered.length > 0) {
        printStudents(filtered);
    } else {
        console.log('Студентов в этой группе не найдено.');
    }
    return filtered;
}

// Примеры использования (для проверки в консоли)
console.log('Для проверки вызови: filterByGroup(groupmates, "БСТ-2201")');
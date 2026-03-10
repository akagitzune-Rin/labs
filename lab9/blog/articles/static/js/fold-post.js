// fold-post.js - Улучшенная версия с CSS-классами

// Находим все кнопки сворачивания на странице
const foldButtons = document.querySelectorAll('.fold-btn');

// Добавляем обработчик клика для каждой кнопки
foldButtons.forEach(button => {
    button.addEventListener('click', function() {
        // Находим родительскую статью
        const post = this.closest('.one-post');
        
        // Переключаем класс folded
        post.classList.toggle('folded');
        
        // Меняем текст кнопки в зависимости от состояния
        if (post.classList.contains('folded')) {
            this.textContent = 'Развернуть';
        } else {
            this.textContent = 'Свернуть';
        }
    });
});

console.log('fold-post.js подключён успешно!');
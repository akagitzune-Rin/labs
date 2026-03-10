// highlight-post.js - Эффекты с jQuery

$(document).ready(function() {
    console.log('jQuery загружен и готов к работе!');
    
    // Эффект 1: Подсветка поста при наведении
    $('.one-post').hover(
        function() {
            // При наведении курсора
            $(this).animate({
                backgroundColor: 'rgba(76, 175, 80, 0.3)',
                boxShadow: '0 0 30px rgba(76, 175, 80, 0.5)'
            }, 300);
        },
        function() {
            // При уходе курсора
            $(this).animate({
                backgroundColor: 'rgba(13, 31, 13, 0.6)',
                boxShadow: '0 5px 20px rgba(0, 0, 0, 0.3)'
            }, 300);
        }
    );
    
    // Эффект 2: Увеличение логотипа/заголовка при наведении
    $('.site-title').hover(
        function() {
            $(this).animate({
                fontSize: '2em',
                textShadow: '0 0 30px rgba(139, 195, 74, 0.8)'
            }, 200);
        },
        function() {
            $(this).animate({
                fontSize: '1.8em',
                textShadow: '0 0 15px rgba(139, 195, 74, 0.5)'
            }, 200);
        }
    );
    
    console.log('highlight-post.js подключён успешно!');
});
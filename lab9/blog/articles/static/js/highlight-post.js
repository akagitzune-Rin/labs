// highlight-post.js - Эффекты с jQuery (Лабораторная 8)

$(document).ready(function() {
    console.log('jQuery загружен и готов к работе!');
    
    // Эффект 1: Подсветка поста при наведении (через one-post-shadow)
    $('.one-post').hover(
        function() {
            // При наведении - анимируем opacity тени
            $(this).find('.one-post-shadow').stop(true).animate({
                opacity: '0.3'
            }, 300);
        },
        function() {
            // При уходе - возвращаем прозрачность
            $(this).find('.one-post-shadow').stop(true).animate({
                opacity: '0'
            }, 300);
        }
    );
    
    // Эффект 2: Увеличение логотипа при наведении
    $('.site-title').hover(
        function() {
            $(this).stop(true).animate({
                fontSize: '2em',
                textShadow: '0 0 30px rgba(139, 195, 74, 0.8)'
            }, 200);
        },
        function() {
            $(this).stop(true).animate({
                fontSize: '1.8em',
                textShadow: '0 0 15px rgba(139, 195, 74, 0.5)'
            }, 200);
        }
    );
    
    console.log('highlight-post.js подключён успешно!');
});
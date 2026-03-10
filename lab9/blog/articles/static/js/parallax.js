// parallax.js - Эффект параллакса для 6 листьев

$(document).ready(function() {
    console.log('Parallax эффект загружен!');
    
    $(window).on('scroll', function() {
        var scrollTop = $(this).scrollTop();
        
        // Двигаем каждый лист с разной скоростью
        $('.parallax-icon').each(function() {
            var $icon = $(this);
            var speed = $icon.data('speed');  // 0.1, 0.2, 0.3, 0.4, 0.5, 0.6
            var yPos = scrollTop * speed;
            
            $icon.css('transform', 'translateY(' + yPos + 'px)');
        });
        
        // Параллакс для логотипа
        var logoSpeed = 0.15;
        var logoY = scrollTop * logoSpeed;
        $('.site-title').css('transform', 'translateY(' + logoY + 'px)');
    });
    
    console.log('Parallax.js работает корректно!');
});
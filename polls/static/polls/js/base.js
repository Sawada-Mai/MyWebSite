$(document).ready(function() {
  $('.slider').slick({
     // ここにスライダーの設定を記述します
     autoplay: true,          // 自動再生を有効にします
     autoplaySpeed: 3000,     // 自動再生のスピードを設定します（ミリ秒単位）
     infinite: true,
     centerMode: true,
     variableWidth: true,
     dots: true,
  });
});


  function fadeAnime(){
  // flipLeft
  $('.gallery li').each(function(){ 
      var elemPos = $(this).offset().top;
      var scroll = $(window).scrollTop();
      var windowHeight = $(window).height();
      if (scroll >= elemPos - windowHeight){
          $(this).addClass('flipLeft');
      }else{
          $(this).removeClass('flipLeft');
      }
  });
  }
  
  // 画面をスクロールをしたら動かしたい場合の記述
    $(window).scroll(function (){
      fadeAnime();/* アニメーション用の関数を呼ぶ*/
    });// ここまで画面をスクロールをしたら動かしたい場合の記述
  
  // ページが読み込まれたらすぐに動かしたい場合の記述
    $(window).on('load', function(){
      fadeAnime();/* アニメーション用の関数を呼ぶ*/
    });// ここまでページが読み込まれたらすぐに動かしたい場合の記述
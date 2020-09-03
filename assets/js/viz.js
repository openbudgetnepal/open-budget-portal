
(function ($) {

  "use strict";

  $(document).ready(function () {
    

    function scroll_header(){
      //header-bg change on scroll
      $(".smooth-scroll").scroll(function(){
        if($(".smooth-scroll").scrollTop() > 200){
            $("header").addClass("scroll-header");
            $("footer").addClass("scroll-footer");
        }
        else{
            $("header").removeClass("scroll-header");
            $("footer").addClass("scroll-footer");
        }
      })
    }
    scroll_header();

    function scroll_header1(){
      //header-bg change on scroll
      $(window).scroll(function(){
        if($(window).scrollTop() > 100){
            $("header").addClass("scroll-header");
        }
        else{
            $("header").removeClass("scroll-header");
        }
      })
    }
    scroll_header1();

    function scroll_top(){
      $(".scroll-top").click(function() {
        $("html, body").animate({ scrollTop: 0 }, "slow");
        return false;
      });
    }
    scroll_top();

    function header_li(){
      $('.menu ul li').on('click', 'a', function(){
        if($(this).closest('a').next().hasClass('active')){
          $('.menu ul li a').removeClass('active');
      }
      else{
        $('.menu ul li a').removeClass('active');
      }
      $(this).closest('a').addClass('active');
      })
    }
    header_li();

    function toggle_button() {
      $('.header-in .toggle-button').on('click', function () {
        $(this).toggleClass('active');
        $('body').toggleClass('Is-toggle');
      });
    }
    toggle_button();

  });

  /* function shuffle_text(){
    const text = baffle('.budget-item span');
    text.set({
      characters: 'sjfka9849832-', 
      speed: 100
    });
    text.start();
    text.reveal(10000);
  }
  shuffle_text(); */
  function pagination(){
    $('.pagination').on('click', 'a', function(){
      if($(this).closest('a').next().hasClass('current')){
        $('.pagination a').removeClass('current');
    }
    else{
      $('.pagination a').removeClass('current');
    }
    $(this).closest('a').addClass('current');
    })
  }
  pagination();

   //pie-chart
   var options = {
    series: [90, 80],
    colors:[ '#7CB5EC', '#22264D'],
    chart: {
      height: '280',
    type: 'pie',
  },
  labels: ['Federal Aid', 'Provincial Resourcesg'],
  legend: {show:false},
  responsive: [{
    breakpoint: 1560,
    options: {
      chart: {
        height: 200,
      },
     
    },
  
  }]
  };

  var chart = new ApexCharts(document.querySelector("#pie-chart"), options);
  chart.render();


})(window.jQuery);


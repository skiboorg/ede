   let review_image=document.getElementById('review_image'), review_title=document.getElementById('review_title'),
            review_description=document.getElementById('review_description'),
            review_shortReview=document.getElementById('review_shortReview'),
            review_fullReview=document.getElementById('review_fullReview'),
            readfullreview_btn = document.getElementById("readfullreview_btn"),
            full_review_div=document.getElementsByClassName('our-help-inner-full-review')[0]
    function changeReview(el) {
            full_review_div.classList.remove('full-review-active')
            readfullreview_btn.innerHTML = "Читать далее...";
            review_image.style.background = "url('"+el.dataset.image+"') no-repeat center"
            review_title.innerText = el.dataset.title
            review_description.innerText = el.dataset.description
            review_shortReview.innerText = el.dataset.shortreview
            review_fullReview.innerHTML = el.dataset.fullreview

    }

     function readOurWorkText() {
        let x = document.getElementById("why-our-work-text")
        x.classList.toggle('why-our-work-text-active')
    }

    function readFullReview() {

        if (readfullreview_btn.innerHTML === "Читать далее...") {
            readfullreview_btn.innerHTML = "Скрыть"
          } else {
            readfullreview_btn.innerHTML = "Читать далее..."
          }
        full_review_div.classList.toggle('full-review-active')

    }

        var mobile = 'false',
            isTestPage = false,
            isDemoPage = true,
            classIn = 'jello',
            classOut = 'rollOut',
            speed = 400,
            doc = document,
            win = window,
            ww = win.innerWidth || doc.documentElement.clientWidth || doc.body.clientWidth,
            fw = getFW(ww),
            initFns = {},
            sliders = new Object(),
            edgepadding = 50,
            gutter = 10;

        function getFW (width) {
            var sm = 400, md = 900, lg = 1400;
            return width < sm ? 150 : width >= sm && width < md ? 200 : width >= md && width < lg ? 300 : 400;
        }
        window.addEventListener('resize', function() { fw = getFW(ww); });

        var options = {
            'our-help-media-slider': {
                container: '',
                items: 4,
                controlsContainer: '#customize-controls',
                autoplay: true,
                autoplayTimeout: 4000,
                speed: 1000,
            },
        }

        for (var i in options) {
            var item = options[i];
            item.container = '#' + i;
            item.swipeAngle = false;
            if (!item.speed) { item.speed = speed; }
            if (document.querySelector(item.container)) {
                sliders[i] = tns(options[i]);
                if (isTestPage && initFns[i]) { initFns[i](); }
            } else if (i.indexOf('responsive') >= 0) {
                if (isTestPage && initFns[i]) { initFns[i](); }
            }
        }

        let mobile_button = document.getElementsByClassName('mobile-toggle')[0]
        let mobile_menu_panel = document.getElementsByClassName('mobile-menu-panel')[0]
        let mobile_menu = document.getElementsByClassName('mobile-menu-panel-inner')[0]
        let arrow_left = document.getElementById('arrow-left')
        let arrow_right = document.getElementById('arrow-right')
        let last_slide = 1
        let current_slide = 1

        mobile_button.onclick = function () {
            this.classList.toggle('mobile-toggle-active')
            mobile_menu_panel.classList.toggle('mobile-menu-panel-active')
            mobile_menu.classList.toggle('mobile-menu-panel-inner-active')
        }


        arrow_left.onclick = function () {
            console.log('left click')
            console.log('last_slide before', last_slide)
            console.log('current_slide before', current_slide)
            let cur_slide = document.getElementsByClassName('slide-active')[0]
            last_slide = current_slide
            if (current_slide-1 < 1){
                current_slide = 4
            }else {
                current_slide -= 1
            }

            changeSlide()
        }

        arrow_right.onclick = function () {
            console.log('right click')
            console.log('last_slide before', last_slide)
            console.log('current_slide before', current_slide)
            let cur_slide = document.getElementsByClassName('slide-active')[0]
            last_slide = current_slide
            if (current_slide+1 > 4){
                current_slide = 1
            }else {
                current_slide += 1
            }
            changeSlide()
        }

        function changeSlide() {
            console.log(current_slide)
            document.getElementById(`step_${last_slide}`).classList.remove('step-active')
            document.getElementById(`slide_${last_slide}`).classList.remove('slide-active')

            setTimeout(function() {
                document.getElementById(`step_${current_slide}`).classList.add('step-active')
                document.getElementById(`slide_${current_slide}`).classList.add('slide-active')

            }, 300);
        }

        function changeSlidebyClick(slide) {
            last_slide = current_slide
            current_slide = slide
            changeSlide()

        }
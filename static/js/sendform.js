  document.getElementsByName('file')[0].addEventListener('change', function () {
        console.log('change')
        let uploaded_files = 'Прикрепленные файлы : '
        for (x of this.files){
            uploaded_files += (x.name + ' ; ')
        }
        this.setAttribute('data-placeholder',uploaded_files)
    })
    function sendForm() {
        let csrfmiddlewaretoken = document.getElementsByName('csrfmiddlewaretoken')[0].defaultValue
        let name = document.getElementsByName('name')[0]
        let email = document.getElementsByName('email')[0]
        let phone = document.getElementsByName('phone')[0]
        let workName = document.getElementsByName('workName')[0]
        let subject = document.getElementsByName('subject')[0]
        let about = document.getElementsByName('about')[0]
        let deadLine = document.getElementsByName('deadLine')[0]
        let volume = document.getElementsByName('volume')[0]
        let file = document.getElementsByName('file')[0].files
        let btn = document.getElementById('form_submit')
        let error_label = document.getElementsByClassName('form-error')[0]
        let req_fields = [workName,phone,email,subject,about,name]
        let all_fields = [workName,phone,email,subject,about,name,deadLine,volume]
        error_label.style.display = 'none'
        btn.setAttribute('disabled', 'disabled');
        btn.firstChild.data = 'Отправка ...'
        for (i of req_fields){
            i.classList.remove("error")
        }
        let fd = new FormData();
        fd.append('csrfmiddlewaretoken',csrfmiddlewaretoken)
        for (i of all_fields){
            fd.append(i.getAttribute('name'),i.value)
        }

        for(var x=0;x<file.length;x++) {
            fd.append('file',file.item(x))


		}


        let xhr = new XMLHttpRequest();
        xhr.open('POST', '/callback/workprice/', true);
        xhr.onload = function () {
            if (JSON.parse(this.response)['result'] === 'ok'){
                btn.firstChild.data = 'Спасибо за обращение, с Вами свяжутся'

            }
            else{
                error_label.style.display = 'block'
                if (JSON.parse(this.response)['errors'] === 'phone'){
                    phone.classList.add("error");
                }

                btn.removeAttribute('disabled')
                btn.firstChild.data = 'Узнать стоимость своей работы'
                for (i of req_fields){
                    if (JSON.parse(this.response)['errors'][i.getAttribute('name')]){
                        i.classList.add("error");
                    }
                }
            }
        };
        xhr.send(fd);
    }
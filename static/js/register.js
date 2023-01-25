function bindEmailCaptchaClick(){
     $("#ecode").click(function (event) {
        var $this = $(this);

        event.preventDefault();
        var email = $("#email").val();
        $.ajax({
            url: "/auth/captcha/email?email="+email,
            method: "GET",
            success: function (result){
                console.log(result);
                var code = result['code'];
                if(code == 200){
                    var countdown = 60;
                    $this.off("click");
                    var timer = setInterval(function(){
                        $this.text(countdown);
                        countdown -= 1;
                        if(countdown == 55){
                            alert("已发送验证码到：" + email);
                        }
                        if(countdown <= 0){
                            clearInterval(timer);
                            $this.text("获取验证码");
                            bindEmailCaptchaClick();
                        }
                    }, 1000);
                }else{
                    alert(result['message']);
                }
            },
            fail: function (result){
                console.log(error);
            }
        })
    });
}


$(function (){
    bindEmailCaptchaClick();
});
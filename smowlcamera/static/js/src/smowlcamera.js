/* Javascript for SMOWLCAMERA*/
function SmowlCameraXblock(runtime, element, settings) {
    $(function ($) {
        if (settings.has_settings){
            var url2222 = window.location.href;
            var url = url2222.split("+").join("%252B");
            var url2 =settings.smowlcamera_url;
            var url3 = "&Course_link="+url;
            var url4 = url2+url3;
            var decoded = url4.replace(/&amp;/g, '&');
            $(element).find('#urlFinal')[0].src =decoded;
            //document.getElementById("").src =decoded ;
        }
    });
}

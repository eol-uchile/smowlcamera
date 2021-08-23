/* Javascript for SMOWLCAMERA*/
function SmowlCameraXblock(runtime, element, settings) {
    $(function ($) {
        if (settings.has_settings){
            if (window.XMLHttpRequest){
                var xmlhttp=new XMLHttpRequest();
            }
            else{
                var xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
            }
            //inicio - nombre de la unidad
            var titulo3 = document.getElementsByClassName("page-header-title");
            var titulo2 = titulo3[0].innerHTML;
            var a = titulo2.includes("<span class");
            if(a){
                var titulo3 = document.getElementsByClassName("title-value");
                var titulo2 = titulo3[0].innerHTML;
            }
            //fin - nombre de la unidad
            var idActivity = settings.parent;
            var idActivity2 = idActivity.split("@");
        
            var urlEntidad2 = window.location.host;
        
            var formData = new FormData();
            formData.append("entity_Name", settings.NombreEntidad);
            formData.append("idModule", titulo2 );
            formData.append("urlEntidad", urlEntidad2 );
            formData.append("idcourseedX", settings.course_id);
            formData.append("idActividadedX", idActivity2[idActivity2.length-1]);
            formData.append("modality", "edxActivity");
            formData.append("swlLicenseKey", settings.swlLicenseKey);
            xmlhttp.open("POST", settings.InsertEDXPOST_URL, false);
            xmlhttp.send(formData);
        }
    });
}

// Add bootstrap model popup listener. For login in PopUp in mainPage
$(document).ready(function() {
    $('#registerPopup').on('shown.bs.modal', function () {
        $('#myInput').focus()
    })

    $('#loginFromRegPopup').click(function() {
        // $('#loginPopup').modal('show')
        $('#registerPopup').modal('hide')
    })
})

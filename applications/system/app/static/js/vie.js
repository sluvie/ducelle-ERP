/**
 * Lib to control page behaviour
 */
class ViePage {
    constructor() {
    }

    /**
     * show popup dialog based on behaviour page
     * @param {*} dialog 
     * @param {*} state 
     * @param {*} callback 
     */
    addedit_dialog(dialog, state = "add", callback = null, params = null) {
        // show loading page
        $.LoadingOverlay("show");

        // state = add
        // state = edit
        // state = view

        switch(state) {
            case "add":
                break;
            case "edit":
                break;
            default:
                // code block
        }

        if (callback) {
            callback(params);
        }

        // anything the state just show the dialog
        $("#" + dialog).modal("show");
        $.LoadingOverlay("hide");
    }


    /**
     * process save dialog
     * @param {*} dialog 
     * @param {*} url 
     * @param {*} params 
     * @param {*} ajaxtype 
     * @param {*} success_callback 
     * @param {*} error_callback 
     * @param {*} text_success 
     * @param {*} text_error 
     */
    save_dialog(dialog, 
        url, params, ajaxtype = 'POST', 
        success_callback = null, error_callback = null, 
        text_success = null, text_error = null) {
        
        // show loading page
        $.LoadingOverlay("show");

        // call the ajax
        $.ajax({
            type: ajaxtype,
            url: url,
            data: JSON.stringify(params),
            contentType: 'application/json',
            dataType: 'json',
            error: function () {
                // call the callback
                if (error_callback) {
                    error_callback(null);
                }
                Swal.fire("Error", '', 'error');
            },
            success: function (data) {
                console.log(data)
                if (data.success) {
                    if (data.success == "1") {
                        // call the callback
                        if (success_callback) {
                            success_callback(data);
                        }
                        // show message success
                        if (text_success) {
                            Swal.fire(text_success, '', 'error');
                        }
                        // close the dialog
                        $("#" + dialog).modal('hide');
                    } else {
                        // call the callback
                        if (error_callback) {
                            error_callback(data);
                        }
                        // show error message
                        Swal.fire(data.message, '', 'error');
                    }
                } else {
                    // call the callback
                    if (error_callback) {
                        error_callback(null);
                    }
                    Swal.fire(text_error, '', 'error');
                }
                $.LoadingOverlay("hide");
            }
        });
    }


    /**
     * read data from database
     * @param {*} url 
     * @param {*} params 
     * @param {*} ajaxtype 
     * @param {*} success_callback 
     * @param {*} error_callback 
     */
    read_data(
        url, params, ajaxtype = 'POST',
        success_callback = null, error_callback = null
    ) {
        // call the ajax
        $.ajax({
            type: ajaxtype,
            url: url,
            data: JSON.stringify(params),
            contentType: 'application/json',
            dataType: 'json',
            error: function () {
                // call the callback
                if (error_callback) {
                    error_callback(null);
                }
                Swal.fire("Error", '', 'error');
            },
            success: function (data) {
                if (data.success) {
                    if (data.success == "1") {
                        // call the callback
                        if (success_callback) {
                            success_callback(data);
                        }
                    } else {
                        // call the callback
                        if (error_callback) {
                            error_callback(data);
                        }
                        // show error message
                        Swal.fire(data.message, '', 'error');
                    }
                } else {
                    // call the callback
                    if (error_callback) {
                        error_callback(null);
                    }
                    Swal.fire(text_error, '', 'error');
                }
            }
        });
    }


    delete_data(
        url, params, ajaxtype = 'POST',
        success_callback = null, error_callback = null,
        text_success = null, text_error = null,
        title_dialog = null, dialog = null
    ) {

        if (!title_dialog) {
            title_dialog = 'Do you want to delete the data?';
        }

        Swal.fire({
            title: title_dialog,
            icon: 'warning',
            showDenyButton: true,
            showCancelButton: true,
            confirmButtonText: `Delete`,
            denyButtonText: `Don't delete`,
        }).then((result) => {
            /* Read more about isConfirmed, isDenied below */
            if (result.isConfirmed) {
                $.LoadingOverlay("show");
                $.ajax({
                    type: ajaxtype,
                    url: url,
                    data: JSON.stringify(params),
                    contentType: 'application/json',
                    dataType: 'json',
                    error: function () {
                        // call the callback
                        if (error_callback) {
                            error_callback(null);
                        }
                        Swal.fire("Error", '', 'error');
                    },
                    success: function (data) {
                        if (data.success) {
                            if (data.success == "1") {
                                if (dialog) {
                                    // close dialog
                                    $("#" + dialog).modal('hide');
                                }
                                // call the callback
                                if (success_callback) {
                                    success_callback(data);
                                }
                            } else {
                                // call the callback
                                if (error_callback) {
                                    error_callback(data);
                                }
                                Swal.fire(data.message, '', 'error');
                            }
                        } else {
                            // call the callback
                            if (error_callback) {
                                error_callback(null);
                            }
                            Swal.fire('Failed to delete', '', 'info');
                        }
                        $.LoadingOverlay("hide");
                    }
                });
            } else if (result.isDenied) {
                Swal.fire('Data are not deleted', '', 'info');
            }
        });
    }
}
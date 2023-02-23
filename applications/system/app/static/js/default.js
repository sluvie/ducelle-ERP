// page
var page = new ViePage();


/**
 * initialize page
 */
$(document).ready(function () {
    console.log("Ready.");

    $(".datepicker").datepicker({
        format: 'yyyy-mm-dd',
        autoclose: true,
        todayHighlight: true
    });
});


/**
 * format date to string yyyy-MM-dd
 * @param {} dateObject 
 * @returns 
 */
$.date = function (dateObject) {
    var d = new Date(dateObject);
    var day = d.getDate();
    var month = d.getMonth() + 1;
    var year = d.getFullYear();
    if (day < 10) {
        day = "0" + day;
    }
    if (month < 10) {
        month = "0" + month;
    }
    var date = year + "-" + month + "-" + day;

    return date;
};


/**
 * format date to string yyyy-MM-dd hh:mm:ss
 * @param {} dateObject 
 * @returns 
 */
$.datetime = function (dateObject) {
    var d = new Date(dateObject);
    var day = d.getDate();
    var month = d.getMonth() + 1;
    var year = d.getFullYear();
    var hour = d.getHours();
    var minute = d.getMinutes();
    var second = d.getSeconds();
    if (day < 10) {
        day = "0" + day;
    }
    if (month < 10) {
        month = "0" + month;
    }
    var date = year + "-" + month + "-" + day + " " + hour + ":" + minute + ":" + second;

    return date;
}


function createDatatable(datatablename) {
    if ($("#" + datatablename)[0]) {
        $("#" + datatablename).DataTable({
            autoWidth: !1,
            responsive: !0,
            lengthMenu: [[15, 30, 45, -1], ["15 Rows", "30 Rows", "45 Rows", "Everything"]],
            language: {
                searchPlaceholder: "Search for records..."
            },
            sDom: '<"dataTables__top"flB<"dataTables_actions">>rt<"dataTables__bottom"ip><"clear">',
            buttons: [{
                extend: "excelHtml5",
                title: "Export Data"
            }, {
                extend: "csvHtml5",
                title: "Export Data"
            }, {
                extend: "print",
                title: "Material Admin"
            }],
            initComplete: function () {
                $("#" + datatablename + "_wrapper").find(".dataTables_actions").html(`
                    <i class="zwicon-more-h" data-toggle="dropdown" />
                    <div class="dropdown-menu dropdown-menu-right">
                        <a data-table-action="print" class="dropdown-item">Print</a>
                        <a data-table-action="fullscreen" class="dropdown-item">Fullscreen</a>
                    <div class="dropdown-divider" />
                        <div class="dropdown-header border-bottom-0 pt-0">
                            <small>Download as</small>
                        </div>
                        <a data-table-action="excel" class="dropdown-item">Excel (.xlsx)</a>
                        <a data-table-action="csv" class="dropdown-item">CSV (.csv)</a>
                    </div>`)
            }
        }),
            $("#" + datatablename + "_wrapper").on("click", "[data-table-action]", function (e) {
                e.preventDefault();
                var t = $(this).data("table-action");
                if ("excel" === t && $("#" + datatablename + "_wrapper").find(".buttons-excel").click(),
                    "csv" === t && $("#" + datatablename + "_wrapper").find(".buttons-csv").click(),
                    "print" === t && $("#" + datatablename + "_wrapper").find(".buttons-print").click(),
                    "fullscreen" === t) {
                    var a = $(this).closest(".card");
                    a.hasClass("card--fullscreen") ? (a.removeClass("card--fullscreen"),
                        $body.removeClass("data-table-toggled")) : (a.addClass("card--fullscreen"),
                            $body.addClass("data-table-toggled"))
                }
            })
    }
}

$(document).on("click", ".navigation__sub", function (e) {
});
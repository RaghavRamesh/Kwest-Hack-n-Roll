var editedDRT = new Object();
$(document)
        .ready(function () {
        	var oTable = $('#exampleDTCF5')
                        .dataTable({
                        bAutoWidth: false,
                        bSortCellsTop: true,
                        BProcessing: true,
                        oLanguage: {
                                sSearch: "Global search: ",
                                sLengthMenu: "Show _MENU_ entries",
                                sZeroRecords: 'No record found <button class="btn btn-danger resetTable">Reset filter</button>'
                        },
                        iDisplayLength: 10,
                        aaSorting: [
                                [3, 'asc']
                        ],
                        aoColumnDefs: [{
                                "aTargets": [0],
                                'bSortable': false,
                                'sWidth': '25px'
                        }, {
                                "aTargets": [1],
                                'sClass': 'bold'
                        }, {
                                "aTargets": [2],
                                'sClass': 'text-left',
                                
                        }, {
                                "aTargets": [3],
                                'sClass': 'text-left',
                                
                        }, {
                                "aTargets": [4],
                                'sClass': 'text-left',
                                
                        }, {
                                "aTargets": [5],
                                'sClass': 'text-left',
                                
                        }, {
                                "aTargets": [6],
                                'sClass': 'text-left',
                                
                        }, {
                                "aTargets": [7],
                                'sClass': 'text-left',
                                
                        },{
                        	"aTargets": [8],
                        	//"bVisible": false
                        }],
                        sPaginationType: 'full_numbers',
                        sDom: "<'row-fluid' <'widget-header' <'span4'l> <'span8'<'table-tool-wrapper'><'table-tool-container'>> > > rti <'row-fluid' <'widget-footer' <'span6' <'table-action-wrapper'>> <'span6'p> >>",

                       
                })
                // Table Filter
                .columnFilter({
                        sPlaceHolder: 'head:after',
                        aoColumns: [
                        null, {
                                type: 'text'
                        },null, {
                                type: 'text'
                        }, {
                                type: 'text'
                        }, {
                                type: 'text'
                        }, {
                                type: 'text'
                        }, {
                                type: 'text'
                        },{
                                type: 'number'
                        }, ]
                });
                // inject to datatable DTCF
            
            
             $('#exampleDTCF5_wrapper .table-tool-wrapper')
                        .html($('#DTCF5_toolBar')
                        .html());
                $('#exampleDTCF5_wrapper .table-action-wrapper')
                        .html($('#DTCF5_actionTable')
                        .html());
                
                $('#exampleDTCF5_length select').select2({
                        minimumResultsForSearch: 2,
                        width: "off"
                });
                $('#exampleDTCF5').dataTable().makeEditable({sUpdateURL:function(value, settings){
     var sib = $(this).siblings(".id");
    var key = $(sib[0]).html();
    var col = $(this).index();
    var val = $(this).find("form textarea").val();
    if (val == undefined){
        val = $(this).find("form input").val();
    }
    var dict;
    if (editedDRT[key] == undefined){
        dict = new Object();
    }
    else {
        dict = editedDRT[key];
    }

    dict[col] = val;
    editedDRT[key] = dict; 
    console.log(editedDRT);    
    return value;
},
    aoColumns:[
    null,
    {tooltip: 'Double click to edit',onblur: 'submit',},
    null,
    {tooltip: 'Double click to edit',onblur: 'submit',},
    {tooltip: 'Double click to edit',onblur: 'submit',},
    {tooltip: 'Double click to edit',onblur: 'submit',type: 'textarea',},
    {tooltip: 'Double click to edit',onblur: 'submit',type: 'textarea',},
    {tooltip: 'Double click to edit',onblur: 'submit',},
    {tooltip: 'Double click to edit',onblur: 'submit',},
],

            });

 $('#exampleDT1')
                        .dataTable({
                        iDisplayLength: 3,
                        sDom: "<'row-fluid' <'span4'l> <'span8'pf> > rt <'row-fluid' <'span12'i> >",
                        aoColumnDefs: [{
                                "aTargets": [0],
                                //"bVisible": false
                        },],

                });
                $('#exampleDT1_length select').select2({
                        minimumResultsForSearch: 6,
                        width: "off"
                });
					
                $('.domainList').dblclick(function(e) {
                    var sib = $(this).html();
                    var url = "/controlpanel/dynamic/"+sib
                    //url = url.replace(/\s+/g, '');
                    //console.log(sib)
                    //console.log(url)

       window.location.replace(url);
        });

$('#exampleDT2')
                        .dataTable({
                        iDisplayLength: 3,
                        sDom: "<'row-fluid' <'span4'l> <'span8'pf> > rt <'row-fluid' <'span12'i> >",
                        aoColumnDefs: [{
                                "aTargets": [0],
                                //"bVisible": false
                        },],

                });
                $('#exampleDT2_length select').select2({
                        minimumResultsForSearch: 6,
                        width: "off"
                });
					


});


/*** -----------------------------------------------------------------------------------------------

	ADMIN TEMPLATE | Boo Admin Template
	----------------------------------------

	JS - Demo DataTable
	
	-------------------------------------------------------------------------------------------------------------------------------- ***/
//var editedDR = new Array();
var editedDR = new Object();
var editedSR = new Object();
var editedCR = new Object();
var editedSC = new Object();
var editedDC = new Object();
$(document)
        .ready(function () {
   
// DATATABLE SETTINGS component-table-boo.html
// ------------------------------------------------------------------------------------------------ * -->
				                // DATATABLE exampleDT
                // -------------------------------------------------------------------------------- * -->
                $('#exampleDT')
                        .dataTable({
                        iDisplayLength: 3,
                        sDom: "<'row-fluid' <'span4'l> <'span8'pf> > rt <'row-fluid' <'span12'i> >",
                        aoColumnDefs: [{
                                "aTargets": [0],
                                //"bVisible": false
                        },],

                });
                $('#exampleDT_length select').select2({
                        minimumResultsForSearch: 6,
                        width: "off"
                });
					$('#exampleDT3')
                        .dataTable({
                        iDisplayLength: 3,
                        sDom: "<'row-fluid' <'span4'l> <'span8'pf> > rt <'row-fluid' <'span12'i> >",
                        aoColumnDefs: [{
                                "aTargets": [0],
                                //"bVisible": false
                        },],

                });
                $('#exampleDT3_length select').select2({
                        minimumResultsForSearch: 6,
                        width: "off"
                });
                $('.domainList').dblclick(function(e) {
                    var sib = $(this).prev().html();
                    var url = "/controlpanel/domain/"+sib
                    url = url.replace(/\s+/g, '');
                    console.log(sib)
                    console.log(url)

       window.location.replace(url);
        });
						
				// DATATABLE exampleDTCF
				// -------------------------------------------------------------------------------- * -->
        		var oTable = $('#exampleDTCF')
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
                        },{
                                "mDataProp": "priority",
                                "aTargets": [1],
                                'sWidth': '45px',
                                
                        },{
                                "aTargets": [2],
                               'sWidth': '25px',
                                'sClass': 'text-left'
                        },{
                                "aTargets": [3],
                                'sWidth': '55px',
                                'sClass': 'text-left'
                        },{
                                "aTargets": [4],
                               'sWidth': '55px',
                                'sClass': 'text-left'
                        },{
                                "aTargets": [5],
                               'sWidth': '105px',
                                'sClass': 'text-left'
                        },{
                                "aTargets": [6],
                                'sWidth': '105px',
                                'sClass': 'text-left'
                        },{
                                "aTargets": [7],
                                'sWidth': '75px',
                                'sClass': 'text-left'
                        },{
                            "aTargets": [8],
                        "bVisible": false} ],
                        sPaginationType: 'full_numbers',
                        sDom: "<'row-fluid' <'widget-header' <'span4'l> <'span8'<'table-tool-wrapper'><'table-tool-container'>> > > rti <'row-fluid' <'widget-footer' <'span6' <'table-action-wrapper'>> <'span6'p> >>",

                        
                })
                // Table Filter
                .columnFilter({
                        sPlaceHolder: 'head:after',
                        aoColumns: [
                        null, {
                                type: 'number',
                        },  {
                                type: 'text'
                        }, {
                                type: 'text'
                        }, {
                                type: 'text'
                        }, {
                                type: 'text'
                        }, {
                                type: 'text'
                        }, {
                                type: 'text'
                        },]
                });
                // inject to datatable DTCF
            
         
             $('#exampleDTCF_wrapper .table-tool-wrapper')
                        .html($('#DTCF_toolBar')
                        .html());
                $('#exampleDTCF_wrapper .table-action-wrapper')
                        .html($('#DTCF_actionTable')
                        .html());
				
				$('#exampleDTCF_length select').select2({
						minimumResultsForSearch: 6,
						width: "off"
				});
$('#exampleDTCF').dataTable().makeEditable({sUpdateURL:function(value, settings){
    var $row = $(this).parents('#exampleDTCF tr');
    var priority = $row.find('.priority').html();
    var col = $(this).index();
    var val = $(this).find("form textarea").val();
    if (val == undefined){
        val = $(this).find("form input").val();
    }
    var dict;
    if (editedDR[priority] == undefined){
        dict = new Object();
    }
    else {
        dict = editedDR[priority];
    }

    dict[col] = val;
    editedDR[priority] = dict;
    return value;

},
    aoColumns:[
    null,
    {tooltip: 'Double click to edit',onblur: 'submit',},
    null,{tooltip: 'Double click to edit',onblur: 'submit',},{tooltip: 'Double click to edit',onblur: 'submit',},
           {
             tooltip: 'Double click to edit',
             type: 'textarea',
             height: '150px',
             onblur: 'submit',
           },
           {
             
             tooltip: 'Double click to edit',
             type: 'textarea',
             onblur: 'submit',
             height: '150px'
           },
           {
            tooltip: 'Double click to edit',onblur: 'submit',
           },
],

               // sUpdateURL:function(value, settings){return (value);}
            });

            
            $('#exampleDTCF1')
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
                                //'sWidth': '65px',
                                'sClass': 'text-left'
                        }, {
                                "aTargets": [2],
                                'sClass': 'text-left ',
                               
                        }, {
                                "aTargets": [3],
                                'sClass': 'text-left ',
                               
                        }, {
                                "aTargets": [4],
                                'sWidth': '25px',
                                'sClass': 'text-center',
                               
                        }, {
                                "aTargets": [5],
                                'sWidth': '25px',
                                'sClass': 'text-center'
                        }, {
                                "aTargets": [6],
                                'sWidth': '25px',
                                'sClass': 'text-center'
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
                        }, {
                                type: 'text'
                        }, {
                                type: 'text'
                        }, ]
                });
                // inject to datatable DTCF
            
            
             $('#exampleDTCF1_wrapper .table-tool-wrapper')
                        .html($('#DTCF_toolBar')
                        .html());
                $('#exampleDTCF1_wrapper .table-action-wrapper')
                        .html($('#DTCF1_actionTable')
                        .html());
				
				$('#exampleDTCF1_length select').select2({
						minimumResultsForSearch: 6,
						width: "off"
				});
        $('#exampleDTCF1').dataTable().makeEditable({sUpdateURL:function(value, settings){
            
var sib = $(this).siblings(".name");
    var name = $(sib[0]).html();
    var col = $(this).index();
    console.log(col);
    var val = $(this).find("form textarea").val();
    if (val == undefined){
        val = $(this).find("form input").val();
    }
    var dict;
    if (editedSR[name] == undefined){
        dict = new Object();
    }
    else {
        dict = editedSR[name];
    }

    dict[col] = val;
    editedSR[name] = dict;
    return value;
},
    aoColumns:[
    null,
    {tooltip: 'Double click to edit',onblur: 'submit',},
           {tooltip: 'Double click to edit',onblur: 'submit',},
           {tooltip: 'Double click to edit',onblur: 'submit',},
           null,null,null,{tooltip: 'Double click to edit',onblur: 'submit',},
],

               // sUpdateURL:function(value, settings){return (value);}
            });
            $('#exampleDTCF2')
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
                                'sWidth': '25px',
                                'sClass': 'text-center'
                        },
                        {
                                "aTargets": [5],
                                'sWidth': '25px',
                                'sClass': 'text-center'
                        },{
                                "aTargets": [6],
                                'sWidth': '25px',
                                'sClass': 'text-center'
                        },],
                        sPaginationType: 'full_numbers',
                        sDom: "<'row-fluid' <'widget-header' <'span4'l> <'span8'<'table-tool-wrapper'><'table-tool-container'>> > > rti <'row-fluid' <'widget-footer' <'span6' <'table-action-wrapper'>> <'span6'p> >>",

                })
                // Table Filter
                .columnFilter({
                        sPlaceHolder: 'head:after',
                        aoColumns: [
                        null, {
                                type: 'text'
                        }, {
                                type: 'text'
                        }, {
                                type: 'text'
                        },]
                });
                // inject to datatable DTCF
            
            
             $('#exampleDTCF2_wrapper .table-tool-wrapper')
                        .html($('#DTCF_toolBar')
                        .html());
                $('#exampleDTCF2_wrapper .table-action-wrapper')
                        .html($('#DTCF2_actionTable')
                        .html());
				
				$('#exampleDTCF2_length select').select2({
						minimumResultsForSearch: 6,
						width: "off"
				});
            
            $('#exampleDTCF2').dataTable().makeEditable({sUpdateURL:function(value, settings){
            
var sib = $(this).siblings(".name");
    var name = $(sib[0]).html();
    var col = $(this).index();
    var val = $(this).find("form textarea").val();
    if (val == undefined){
        val = $(this).find("form input").val();
    }
    var dict;
    if (editedCR[name] == undefined){
        dict = new Object();
    }
    else {
        dict = editedCR[name];
    }

    dict[col] = val;
    editedCR[name] = dict;
    return value;
},
    aoColumns:[
    null,
    {tooltip: 'Double click to edit',onblur: 'submit',},
    {tooltip: 'Double click to edit',onblur: 'submit',},{tooltip: 'Double click to edit',onblur: 'submit',},
           null,null,null,{tooltip: 'Double click to edit',onblur: 'submit',},
],

               // sUpdateURL:function(value, settings){return (value);}
            });

            $('#exampleDTCF3')
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
                                'sWidth': '65px',
                                'sClass': 'bold'
                        },{
                                "aTargets": [2],
                                'sClass': 'text-left',
                                
                        },{
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
                                'sClass': 'text-center',
                                'sWidth': '25px'
                        }, {
                                "aTargets": [7],
                                'sClass': 'text-center',
                                'sWidth': '25px'
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
                        }, {
                                type: 'text'
                        }, {
                                type: 'text'
                        }, {
                                type: 'text'
                        }, {
                                type: 'text'
                        }]
                });
                // inject to datatable DTCF
            
            
             $('#exampleDTCF3_wrapper .table-tool-wrapper')
                        .html($('#DTCF_toolBar')
                        .html());
                $('#exampleDTCF3_wrapper .table-action-wrapper')
                        .html($('#DTCF3_actionTable')
                        .html());
				
				$('#exampleDTCF3_length select').select2({
						minimumResultsForSearch: 6,
						width: "off"
				});
            $('#exampleDTCF3').dataTable().makeEditable({sUpdateURL:function(value, settings){
            
var sib = $(this).siblings(".key");
    var key = $(sib[0]).html();
    var col = $(this).index();
    var val = $(this).find("form textarea").val();
    if (val == undefined){
        val = $(this).find("form input").val();
    }
    var dict;
    if (editedSC[key] == undefined){
        dict = new Object();
    }
    else {
        dict = editedSC[key];
    }

    dict[col] = val;
    editedSC[key] = dict;
    return value;
},
    aoColumns:[
    null,
    {tooltip: 'Double click to edit',onblur: 'submit',},
    {tooltip: 'Double click to edit',onblur: 'submit',},{tooltip: 'Double click to edit',onblur: 'submit',},
    {tooltip: 'Double click to edit',onblur: 'submit',},{tooltip: 'Double click to edit',onblur: 'submit',},
           null,null
],

               // sUpdateURL:function(value, settings){return (value);}
            });
            $('#exampleDTCF4')
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
                                //'sWidth': '100px',
                                'sClass': 'bold'
                        }, {
                                "aTargets": [2],
                                //'sWidth': '100px',
                                'sClass': 'text-left',
                                
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
                        }, {
                                type: 'text'
                        }]
                });
                // inject to datatable DTCF
            
            
             $('#exampleDTCF4_wrapper .table-tool-wrapper')
                        .html($('#DTCF_toolBar')
                        .html());
                $('#exampleDTCF4_wrapper .table-action-wrapper')
                        .html($('#DTCF4_actionTable')
                        .html());
				
				$('#exampleDTCF4_length select').select2({
						minimumResultsForSearch: 2,
						width: "off"
				});
            
           $('#exampleDTCF4').dataTable().makeEditable({sUpdateURL:function(value, settings){
            
    return value;
},
    aoColumns:[
    null,
    {tooltip: 'Double click to edit',onblur: 'submit',},
    {tooltip: 'Double click to edit',onblur: 'submit',},
],

               // sUpdateURL:function(value, settings){return (value);}
            });
                

				
		 
            
           /*$('#exampleDTCF5').dataTable().makeEditable({sUpdateURL:function(value, settings){
            
    return value;
},
    aoColumns:[
    null,
    {tooltip: 'Double click to edit',onblur: 'submit',},
    {tooltip: 'Double click to edit',onblur: 'submit',},
],

               // sUpdateURL:function(value, settings){return (value);}
            });*/
                	
			



});
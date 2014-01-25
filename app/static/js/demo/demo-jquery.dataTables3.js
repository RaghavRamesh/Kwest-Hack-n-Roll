var editedDRT = new Object();
$(document)
        .ready(function () {
        	$('#exampleDTCF6')
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
                                
                        },],
                        sPaginationType: 'full_numbers',
                        sDom: "<'row-fluid' <'widget-header' <'span4'l> <'span8'<'table-tool-wrapper'><'table-tool-container'>> > > rti <'row-fluid' <'widget-footer' <'span6' <'table-action-wrapper'>> <'span6'p> >>",

                       
                })
                // Table Filter
                .columnFilter({
                        sPlaceHolder: 'head:after',
                        aoColumns: [
                        null, {
                                type: 'number'
                        }, {
                                type: 'text'
                        },null,  ]
                });
                // inject to datatable DTCF
            
            
             $('#exampleDTCF6_wrapper .table-tool-wrapper')
                        .html($('#DTCF6_toolBar')
                        .html());
                $('#exampleDTCF6_wrapper .table-action-wrapper')
                        .html($('#DTCF6_actionTable')
                        .html());
                
                $('#exampleDTCF6_length select').select2({
                        minimumResultsForSearch: 2,
                        width: "off"
                });



					


});


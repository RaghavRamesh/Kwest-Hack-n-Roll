var editedDRT = new Object();
$(document)
        .ready(function () {
        	$('#exampleDTCF7')
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
                        },   ]
                });
                // inject to datatable DTCF
            
            
             $('#exampleDTCF7_wrapper .table-tool-wrapper')
                        .html($('#DTCF6_toolBar')
                        .html());
                $('#exampleDTCF7_wrapper .table-action-wrapper')
                        .html($('#DTCF7_actionTable')
                        .html());
                
                $('#exampleDTCF7_length select').select2({
                        minimumResultsForSearch: 2,
                        width: "off"
                });



					


});


// GetProduct by category_id
$(function() {
    $('#category_id').on("change", function () {
        category_id = $(this).val();
        //alert(category_id);
        $.get(
            "/borrows/getBooks",
            {
                category_id: category_id,
            },
            function (data, textStatus, jqXHR) {
                $("#id_book").html(data);
            }
        );
    } );
});

function print(){
    all_tables.print();
}
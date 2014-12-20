$('#likes').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/rango/like_category/', {category_id : catid}, function(data){
        $('#like_count').html(data);
        $('#likes').hide();
    })
});

$('#suggestion').keyup(function () {
    var query;
    query = $(this).val();
    $.get('/rango/suggest_category/', {'suggestion' : query}, function (data) {
        $('#cats').html(data);
    });
});

$('#add_page').click(function(){
    var catename;
    catname = $(this).attr("data-catname");
    console.log(catname);
    $.get('/rango/category/'+catname+'/add_page/', function(data){
        console.log(data);
    });
});

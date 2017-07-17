$(document).on('ready',function(){
  console.log("eso es lo q hay jajajaja");
 deleteArticulos();
  $('#id_proveedor').on('change',function(event){
    if($(this).val().length >0 ){
      getArticulos($(this).val(), $(this));
    }else{
        deleteArticulos();
    }
  });
});

function deleteArticulos(){
  $('#id_articulo').material_select('destroy');
  $('#id_articulo').html("<option class>--------</option>")
  $('#id_articulo').prop('disabled', true);
  $('#id_articulo').material_select('destroy');
}

function getArticulos(id_proveedor,nodo){
  $.ajax({
    url:"/inventario/ws/articulos/proveedor/?q="+id_proveedor,
    method:'get',
    dataType:'json',
    success: function(data){
      console.log(data['object_list']);
      element = data['object_list'];
      var men ="";
      console.log("tamaño de los elementos  --> "+element.length);
      if(element.length > 0){
        for (var i=0; i < element.length; i++){
          men+="<option value=\""+element[i].id+"\">"+element[i].codigo+" "+element[i].nombre+"</option>";
        }
        console.log("mensaje ---> ",men);
        $('#id_articulo').material_select('destroy');
        $('#id_articulo').html("<option class>--------</option>")
        $('#id_articulo').append(men);
        $('#id_articulo').prop('disabled', false);
        $('#id_articulo').material_select();
      }else{
        deleteArticulos();
      }
    }
  });
}

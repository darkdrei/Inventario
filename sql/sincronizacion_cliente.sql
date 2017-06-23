create or replace function sincronizar_cliente(_data json) returns boolean as $$
declare
	factura record;
    descri record;
    articulo_tem record;
    factura_id integer;
    resta_articulo real:=0;
    total_procedimiento real:=0;
begin
	for factura in select * from json_each(_data) loop
    	insert into venta_factura(fecha,subtotal,iva,total,paga,estado,impoconsumo)
        	values
            	(cast(factura.value::json->>'fecha' as timestamp with time zone),0,0,0,true,true,0) returning id into factura_id;
                for descri in select * from json_populate_recordset(null::descripcion,cast(factura.value::json->>'descripcion' as json)) loop
                	select * from inventario_activo where id=descri.articulo limit 1 into articulo_tem;
                    if articulo_tem.id is not null then
                    	if articulo_tem.existencias >= descri.cantidad then
                        	resta_articulo:= descri.cantidad;
                         else
                            resta_articulo:= articulo_tem.existencia;
                         end if;
                        if articulo_tem.tipo= 1 then
                        	update inventario_activo set existencias= articulo_tem.existencias-resta_articulo where id=articulo_tem.id;
                        elsif articulo_tem.tipo = 2 then
                        	update inventario_activo set existencias= articulo_tem.existencias-resta_articulo where id=articulo_tem.id;
                        end if;
                        insert into venta_detalle (cantidad,valor_unitario,total,articulo_id,factura_id) values(resta_articulo,articulo_tem.precio_venta,resta_articulo*articulo_tem.precio_venta,articulo_tem.id,factura_id);
                        total_procedimiento:=total_procedimiento + resta_articulo*articulo_tem.precio_venta;
                    end if;
                end loop;
                update venta_factura set total= total_procedimiento where id=factura_id;
    end loop;
    return true;
end;
$$language plpgsql;

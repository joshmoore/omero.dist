--
-- Copyright 2011 Glencoe Software, Inc. All rights reserved.
-- Use is subject to license terms supplied in LICENSE.txt
--

--
-- This SQL script will move all data to a single group and
-- user pair. This can be used to make a unified "public DB"
-- in which all data is visible.
--
-- See #6305 for more information.
--
-- Usage:
--
--   psql -vGRP=3 -vUSR=20 -f omero-4.1-all-public.sql <my-database>
--


begin;
\timing
create or replace function omero_41_move_to_group(GRP int8, USR int8) returns setof text as $$
declare
    rec record;
    sql text;
begin

    for rec in select table_name as tbl FROM information_schema.columns WHERE column_name ='group_id' loop
        sql := 'update ' || rec.tbl || ' set group_id = '|| GRP ||', owner_id = ' || USR;
        execute sql;
        return next rec.tbl || ' updated for user ' || USR || ' in group ' || GRP;
    end loop;

    return;

end; $$ language plpgsql;
select * from omero_41_move_to_group(:GRP, :USR) as report;
drop function omero_41_move_to_group(int8, int8);
commit;

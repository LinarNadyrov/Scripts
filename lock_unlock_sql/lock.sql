\c "name db"
update tbl_user set is_locked = true where labels not like '%TEST%';

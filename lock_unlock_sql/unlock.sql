\c tadb
update tbl_user set is_locked = false where labels not like '%INACTIVE%';

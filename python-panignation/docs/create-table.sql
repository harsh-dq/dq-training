CREATE TABLE public.formdata(
    id serial,
    firstname varchar,
    lastname varchar,
    email varchar,
    comments text,
    createdon timestamp with time zone DEFAULT now()
);
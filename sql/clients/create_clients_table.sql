CREATE TABLE IF NOT EXISTS clients (
    id integer,
    name text,
    document_type text check(document_type in ('CPF', 'CNPJ')) not null,
    document text not null,
    emails text,
    facilities text
)
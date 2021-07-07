def post_data(request_json, pg):
    try:
        require_order_list = [
            "firstname",
            "lastname",
            "email",
            "comments",
        ]
        dict_data = {k: request_json[k] for k in require_order_list}
        values = [y for x, y in dict_data.items()]
        sql = """
                INSERT INTO formdata (firstname, lastname, email, comments )
                 VALUES (%s,%s,%s,%s); 
            """
        pg.execute(sql, values)
        return {"success": True, "message": "Successfully inserted record"}
    except Exception as e:
        return {"error": str(e), "success": False}


def get_data(pg, offset, limit):
    try:
        sql = """
                select firstname,lastname,email,comments,createdon 
                from formdata
                order by  createdon desc
                LIMIT {limit} OFFSET {offset} ;
                """.format(
            limit=limit, offset=offset
        )
        pg.execute(sql)
        query_result = pg.fetchall()
        data = [dict(row) for row in query_result]

        # get total values
        sql = "select count(*) from formdata"
        pg.execute(sql)
        query_result = pg.fetchone()
        result = {
            "total_cont": query_result[0],
            "count": 5,
            "total_page": query_result[0] // 5 if query_result[0] % 5 == 0 else (query_result[0] // 5) + 1,
            "data": data
        }
        return result
    except Exception as e:
        return {"error": str(e), "success": False}



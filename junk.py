        try:
            items = Todo.fetch_all()
            # if len(items) == 0:
                # ns_todos.abort(404, e.__doc__, status = "Todo items do not exist", statusCode = "404")
            data = {
				"status": "Matches retrieved",
				"Matches" : items
			}
            return todos_schema.dumps(data)
        except KeyError as e:
            ns_todos.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
        except Exception as e:
            ns_todos.abort(400, e.__doc__, status = "Could not retrieve information", statusCode = "400")

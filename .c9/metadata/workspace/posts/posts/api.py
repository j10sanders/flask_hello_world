{"filter":false,"title":"api.py","tooltip":"/posts/posts/api.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":23,"column":5},"end":{"row":23,"column":6},"action":"insert","lines":["o"],"id":112}],[{"start":{"row":23,"column":6},"end":{"row":23,"column":7},"action":"insert","lines":["d"],"id":113}],[{"start":{"row":23,"column":7},"end":{"row":23,"column":8},"action":"insert","lines":["y"],"id":114}],[{"start":{"row":23,"column":34},"end":{"row":23,"column":39},"action":"remove","lines":["title"],"id":115},{"start":{"row":23,"column":34},"end":{"row":23,"column":35},"action":"insert","lines":["b"]}],[{"start":{"row":23,"column":35},"end":{"row":23,"column":36},"action":"insert","lines":["o"],"id":116}],[{"start":{"row":23,"column":36},"end":{"row":23,"column":37},"action":"insert","lines":["d"],"id":117}],[{"start":{"row":23,"column":37},"end":{"row":23,"column":38},"action":"insert","lines":["y"],"id":118}],[{"start":{"row":27,"column":7},"end":{"row":27,"column":12},"action":"remove","lines":["title"],"id":119},{"start":{"row":27,"column":7},"end":{"row":27,"column":8},"action":"insert","lines":["b"]}],[{"start":{"row":27,"column":8},"end":{"row":27,"column":9},"action":"insert","lines":["o"],"id":120}],[{"start":{"row":27,"column":9},"end":{"row":27,"column":10},"action":"insert","lines":["d"],"id":121}],[{"start":{"row":27,"column":10},"end":{"row":27,"column":11},"action":"insert","lines":["y"],"id":122}],[{"start":{"row":28,"column":56},"end":{"row":28,"column":61},"action":"remove","lines":["title"],"id":131},{"start":{"row":28,"column":56},"end":{"row":28,"column":57},"action":"insert","lines":["b"]}],[{"start":{"row":28,"column":57},"end":{"row":28,"column":58},"action":"insert","lines":["o"],"id":132}],[{"start":{"row":28,"column":58},"end":{"row":28,"column":59},"action":"insert","lines":["d"],"id":133}],[{"start":{"row":28,"column":59},"end":{"row":28,"column":60},"action":"insert","lines":["y"],"id":134}],[{"start":{"row":25,"column":25},"end":{"row":25,"column":26},"action":"insert","lines":["b"],"id":135}],[{"start":{"row":25,"column":26},"end":{"row":25,"column":27},"action":"insert","lines":["o"],"id":136}],[{"start":{"row":25,"column":27},"end":{"row":25,"column":28},"action":"insert","lines":["d"],"id":137}],[{"start":{"row":25,"column":28},"end":{"row":25,"column":29},"action":"insert","lines":["y"],"id":138}],[{"start":{"row":25,"column":29},"end":{"row":25,"column":30},"action":"insert","lines":[" "],"id":139}],[{"start":{"row":25,"column":30},"end":{"row":25,"column":31},"action":"insert","lines":["o"],"id":140}],[{"start":{"row":25,"column":31},"end":{"row":25,"column":32},"action":"insert","lines":["f"],"id":141}],[{"start":{"row":25,"column":32},"end":{"row":25,"column":33},"action":"insert","lines":[" "],"id":142}],[{"start":{"row":23,"column":4},"end":{"row":23,"column":45},"action":"remove","lines":["body_like = request.args.get(\"body_like\")"],"id":143}],[{"start":{"row":15,"column":47},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":144},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":16,"column":4},"end":{"row":16,"column":45},"action":"insert","lines":["body_like = request.args.get(\"body_like\")"],"id":145}],[{"start":{"row":22,"column":4},"end":{"row":23,"column":0},"action":"insert","lines":["",""],"id":146},{"start":{"row":23,"column":0},"end":{"row":23,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":23,"column":4},"end":{"row":24,"column":0},"action":"insert","lines":["",""],"id":147},{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":28,"column":3},"end":{"row":29,"column":38},"action":"remove","lines":[" # Get and filter the body of posts from the database","    posts = session.query(models.Post)"],"id":148}],[{"start":{"row":28,"column":2},"end":{"row":28,"column":3},"action":"remove","lines":[" "],"id":149}],[{"start":{"row":28,"column":1},"end":{"row":28,"column":2},"action":"remove","lines":[" "],"id":150}],[{"start":{"row":28,"column":0},"end":{"row":28,"column":1},"action":"remove","lines":[" "],"id":151}],[{"start":{"row":27,"column":0},"end":{"row":28,"column":0},"action":"remove","lines":["",""],"id":152}],[{"start":{"row":26,"column":4},"end":{"row":27,"column":0},"action":"remove","lines":["",""],"id":153}],[{"start":{"row":26,"column":0},"end":{"row":26,"column":4},"action":"remove","lines":["    "],"id":154}],[{"start":{"row":25,"column":0},"end":{"row":26,"column":0},"action":"remove","lines":["",""],"id":155}],[{"start":{"row":22,"column":4},"end":{"row":23,"column":67},"action":"insert","lines":[" if body_like:","        posts = posts.filter(models.Post.title.contains(body_like))"],"id":156}],[{"start":{"row":22,"column":4},"end":{"row":22,"column":5},"action":"remove","lines":[" "],"id":157}],[{"start":{"row":25,"column":2},"end":{"row":25,"column":3},"action":"remove","lines":[" "],"id":158}],[{"start":{"row":25,"column":1},"end":{"row":25,"column":2},"action":"remove","lines":[" "],"id":159}],[{"start":{"row":25,"column":0},"end":{"row":25,"column":1},"action":"remove","lines":[" "],"id":160}],[{"start":{"row":24,"column":4},"end":{"row":25,"column":0},"action":"remove","lines":["",""],"id":161}],[{"start":{"row":24,"column":4},"end":{"row":24,"column":5},"action":"remove","lines":[" "],"id":162}],[{"start":{"row":26,"column":4},"end":{"row":28,"column":42},"action":"remove","lines":["if body_like:","        posts = posts.filter(models.Post.title.contains(body_like))","    posts = posts.order_by(models.Post.id)"],"id":163}],[{"start":{"row":26,"column":0},"end":{"row":26,"column":4},"action":"remove","lines":["    "],"id":164}],[{"start":{"row":25,"column":0},"end":{"row":26,"column":0},"action":"remove","lines":["",""],"id":165}],[{"start":{"row":8,"column":29},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":166}],[{"start":{"row":9,"column":0},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":167}],[{"start":{"row":9,"column":0},"end":{"row":10,"column":0},"action":"remove","lines":["",""],"id":169}],[{"start":{"row":24,"column":41},"end":{"row":24,"column":46},"action":"remove","lines":["title"],"id":170},{"start":{"row":24,"column":41},"end":{"row":24,"column":42},"action":"insert","lines":["b"]}],[{"start":{"row":24,"column":42},"end":{"row":24,"column":43},"action":"insert","lines":["o"],"id":171}],[{"start":{"row":24,"column":43},"end":{"row":24,"column":44},"action":"insert","lines":["d"],"id":172}],[{"start":{"row":24,"column":44},"end":{"row":24,"column":45},"action":"insert","lines":["y"],"id":173}],[{"start":{"row":68,"column":0},"end":{"row":84,"column":48},"action":"insert","lines":["@app.route(\"/api/posts\", methods=[\"POST\"])","@decorators.accept(\"application/json\")","def posts_post():","    \"\"\" Add a new post \"\"\"","    data = request.json","","    # Add the post to the database","    post = models.Post(title=data[\"title\"], body=data[\"body\"])","    session.add(post)","    session.commit()","","    # Return a 201 Created, containing the post as JSON and with the","    # Location header set to the location of the post","    data = json.dumps(post.as_dictionary())","    headers = {\"Location\": url_for(\"post_get\", id=post.id)}","    return Response(data, 201, headers=headers,","                    mimetype=\"application/json\")"],"id":174}],[{"start":{"row":69,"column":38},"end":{"row":70,"column":0},"action":"insert","lines":["",""],"id":175}],[{"start":{"row":70,"column":0},"end":{"row":70,"column":38},"action":"insert","lines":["@decorators.accept(\"application/json\")"],"id":176}],[{"start":{"row":70,"column":12},"end":{"row":70,"column":18},"action":"remove","lines":["accept"],"id":177},{"start":{"row":70,"column":12},"end":{"row":70,"column":13},"action":"insert","lines":["r"]}],[{"start":{"row":70,"column":13},"end":{"row":70,"column":14},"action":"insert","lines":["e"],"id":178}],[{"start":{"row":70,"column":14},"end":{"row":70,"column":15},"action":"insert","lines":["q"],"id":179}],[{"start":{"row":70,"column":15},"end":{"row":70,"column":16},"action":"insert","lines":["u"],"id":180}],[{"start":{"row":70,"column":16},"end":{"row":70,"column":17},"action":"insert","lines":["i"],"id":181}],[{"start":{"row":70,"column":17},"end":{"row":70,"column":18},"action":"insert","lines":["r"],"id":182}],[{"start":{"row":70,"column":18},"end":{"row":70,"column":19},"action":"insert","lines":["e"],"id":183}],[{"start":{"row":10,"column":0},"end":{"row":17,"column":1},"action":"insert","lines":["# JSON Schema describing the structure of a post","post_schema = {","    \"properties\": {","        \"title\" : {\"type\" : \"string\"},","        \"body\": {\"type\": \"string\"}","    },","    \"required\": [\"title\", \"body\"]","}"],"id":184}],[{"start":{"row":17,"column":1},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":185}],[{"start":{"row":18,"column":0},"end":{"row":19,"column":0},"action":"insert","lines":["",""],"id":186}],[{"start":{"row":76,"column":0},"end":{"row":94,"column":48},"action":"remove","lines":["","@app.route(\"/api/posts\", methods=[\"POST\"])","@decorators.accept(\"application/json\")","@decorators.require(\"application/json\")","def posts_post():","    \"\"\" Add a new post \"\"\"","    data = request.json","","    # Add the post to the database","    post = models.Post(title=data[\"title\"], body=data[\"body\"])","    session.add(post)","    session.commit()","","    # Return a 201 Created, containing the post as JSON and with the","    # Location header set to the location of the post","    data = json.dumps(post.as_dictionary())","    headers = {\"Location\": url_for(\"post_get\", id=post.id)}","    return Response(data, 201, headers=headers,","                    mimetype=\"application/json\")"],"id":187},{"start":{"row":76,"column":0},"end":{"row":77,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":77,"column":0},"end":{"row":102,"column":48},"action":"insert","lines":["@app.route(\"/api/posts\", methods=[\"POST\"])","@decorators.accept(\"application/json\")","@decorators.require(\"application/json\")","def posts_post():","    \"\"\" Add a new post \"\"\"","    data = request.json","","    # Check that the JSON supplied is valid","    # If not you return a 422 Unprocessable Entity","    try:","        validate(data, post_schema)","    except ValidationError as error:","        data = {\"message\": error.message}","        return Response(json.dumps(data), 422, mimetype=\"application/json\")","","    # Add the post to the database","    post = models.Post(title=data[\"title\"], body=data[\"body\"])","    session.add(post)","    session.commit()","","    # Return a 201 Created, containing the post as JSON and with the","    # Location header set to the location of the post","    data = json.dumps(post.as_dictionary())","    headers = {\"Location\": url_for(\"post_get\", id=post.id)}","    return Response(data, 201, headers=headers,","                    mimetype=\"application/json\")"],"id":188}],[{"start":{"row":102,"column":48},"end":{"row":103,"column":0},"action":"insert","lines":["",""],"id":189},{"start":{"row":103,"column":0},"end":{"row":103,"column":20},"action":"insert","lines":["                    "]}],[{"start":{"row":103,"column":20},"end":{"row":104,"column":0},"action":"insert","lines":["",""],"id":190},{"start":{"row":104,"column":0},"end":{"row":104,"column":20},"action":"insert","lines":["                    "]}],[{"start":{"row":104,"column":16},"end":{"row":104,"column":20},"action":"remove","lines":["    "],"id":191}],[{"start":{"row":104,"column":12},"end":{"row":104,"column":16},"action":"remove","lines":["    "],"id":192}],[{"start":{"row":104,"column":8},"end":{"row":104,"column":12},"action":"remove","lines":["    "],"id":193}],[{"start":{"row":104,"column":4},"end":{"row":104,"column":8},"action":"remove","lines":["    "],"id":194}],[{"start":{"row":104,"column":0},"end":{"row":104,"column":4},"action":"remove","lines":["    "],"id":195}],[{"start":{"row":104,"column":0},"end":{"row":107,"column":17},"action":"insert","lines":["@app.route(\"/api/posts\", methods=[\"POST\"])","@decorators.accept(\"application/json\")","@decorators.require(\"application/json\")","def posts_post():"],"id":196}],[{"start":{"row":104,"column":36},"end":{"row":104,"column":39},"action":"remove","lines":["OST"],"id":197},{"start":{"row":104,"column":36},"end":{"row":104,"column":37},"action":"insert","lines":["U"]}],[{"start":{"row":104,"column":37},"end":{"row":104,"column":38},"action":"insert","lines":["T"],"id":198}],[{"start":{"row":107,"column":0},"end":{"row":107,"column":4},"action":"insert","lines":["    "],"id":199}],[{"start":{"row":107,"column":0},"end":{"row":107,"column":4},"action":"remove","lines":["    "],"id":200}],[{"start":{"row":107,"column":17},"end":{"row":108,"column":0},"action":"insert","lines":["",""],"id":201},{"start":{"row":108,"column":0},"end":{"row":108,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":107,"column":10},"end":{"row":107,"column":14},"action":"remove","lines":["post"],"id":202},{"start":{"row":107,"column":10},"end":{"row":107,"column":11},"action":"insert","lines":["e"]}],[{"start":{"row":107,"column":11},"end":{"row":107,"column":12},"action":"insert","lines":["d"],"id":203}],[{"start":{"row":107,"column":12},"end":{"row":107,"column":13},"action":"insert","lines":["i"],"id":204}],[{"start":{"row":107,"column":13},"end":{"row":107,"column":14},"action":"insert","lines":["t"],"id":205}],[{"start":{"row":108,"column":4},"end":{"row":129,"column":48},"action":"insert","lines":["\"\"\" Add a new post \"\"\"","    data = request.json","","    # Check that the JSON supplied is valid","    # If not you return a 422 Unprocessable Entity","    try:","        validate(data, post_schema)","    except ValidationError as error:","        data = {\"message\": error.message}","        return Response(json.dumps(data), 422, mimetype=\"application/json\")","","    # Add the post to the database","    post = models.Post(title=data[\"title\"], body=data[\"body\"])","    session.add(post)","    session.commit()","","    # Return a 201 Created, containing the post as JSON and with the","    # Location header set to the location of the post","    data = json.dumps(post.as_dictionary())","    headers = {\"Location\": url_for(\"post_get\", id=post.id)}","    return Response(data, 201, headers=headers,","                    mimetype=\"application/json\")"],"id":206}],[{"start":{"row":108,"column":8},"end":{"row":108,"column":18},"action":"remove","lines":["Add a new "],"id":207},{"start":{"row":108,"column":8},"end":{"row":108,"column":9},"action":"insert","lines":["E"]}],[{"start":{"row":108,"column":9},"end":{"row":108,"column":10},"action":"insert","lines":["d"],"id":208}],[{"start":{"row":108,"column":10},"end":{"row":108,"column":11},"action":"insert","lines":["i"],"id":209}],[{"start":{"row":108,"column":11},"end":{"row":108,"column":12},"action":"insert","lines":["t"],"id":210}],[{"start":{"row":108,"column":12},"end":{"row":108,"column":13},"action":"insert","lines":[" "],"id":211}],[{"start":{"row":108,"column":13},"end":{"row":108,"column":14},"action":"insert","lines":["a"],"id":212}],[{"start":{"row":108,"column":14},"end":{"row":108,"column":15},"action":"insert","lines":[" "],"id":213}],[{"start":{"row":108,"column":23},"end":{"row":109,"column":0},"action":"insert","lines":["",""],"id":214},{"start":{"row":109,"column":0},"end":{"row":109,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":109,"column":4},"end":{"row":110,"column":0},"action":"insert","lines":["",""],"id":215},{"start":{"row":110,"column":0},"end":{"row":110,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":110,"column":4},"end":{"row":115,"column":63},"action":"insert","lines":["# check if the post exists, if not return a 404 with a helpful message","    post = session.query(models.Post).get(id)","    if not post:","        message = \"Could not find post with id {}\".format(id)","        data = json.dumps({\"message\": message})","        return Response(data, 404, mimetype=\"application/json\")"],"id":216}],[{"start":{"row":115,"column":63},"end":{"row":116,"column":0},"action":"insert","lines":["",""],"id":217},{"start":{"row":116,"column":0},"end":{"row":116,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":128,"column":4},"end":{"row":130,"column":20},"action":"remove","lines":["post = models.Post(title=data[\"title\"], body=data[\"body\"])","    session.add(post)","    session.commit()"],"id":218},{"start":{"row":128,"column":4},"end":{"row":130,"column":20},"action":"insert","lines":["post.title = data[\"title\"]","    post.body = data[\"body\"]","    session.commit()"]}],[{"start":{"row":107,"column":15},"end":{"row":107,"column":16},"action":"insert","lines":["i"],"id":219}],[{"start":{"row":107,"column":16},"end":{"row":107,"column":17},"action":"insert","lines":["d"],"id":223}],[{"start":{"row":104,"column":0},"end":{"row":104,"column":41},"action":"remove","lines":["@app.route(\"/api/posts\", methods=[\"PUT\"])"],"id":224},{"start":{"row":104,"column":0},"end":{"row":104,"column":50},"action":"insert","lines":["@app.route(\"/api/posts/<int:id>\", methods=[\"PUT\"])"]}]]},"ace":{"folds":[],"scrolltop":1380.727207183838,"scrollleft":0,"selection":{"start":{"row":104,"column":50},"end":{"row":104,"column":50},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1450225522175,"hash":"296087727360367d31190d905b38377b63673462"}
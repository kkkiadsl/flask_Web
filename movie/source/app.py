from flask import Flask, request, Response
from flask_restx import Resource, Api, fields
from flask import abort, jsonify
from flask import render_template, make_response


app = Flask(__name__)
api = Api(app)

ns_movie = api.namespace('ns_movie', description='movie APIs')

movie_info = {
'Evil Dead 2013':'《이블 데드》(영어: Evil Dead)는 2013년 공개된 미국의 공포 영화이다. 샘 레이미의 동명 영화를 바탕으로 페데 알바레스 감독이 리메이크하였다.',
'Annabelle Creation (2017)':'2017년에 워너 브라더스에서 데이비드 F. 샌드버그 감독이 만든 애나벨 시리즈의 두 번째 작품. 컨저링 시리즈를 만든 제임스 완이 제작을 맡았고, 컨저링 유니버스에 속한 작품이다. (컨저링 유니버스는 컨저링, 애나벨, 더 넌 시리즈가 통합된 하나의 세계관을 말한다)',
'Insidious The Last Key (2018)':'2018년에 애덤 로비텔 감독이 만든 인시디어스 시리즈의 4번째 작품. 내용은 1953년에 뉴 멕시코에서 부모님과 남동생 등 가족과 함께 살던 엘리스 레이니어가 귀신을 보는 능력을 가졌는데 그로 인해 악마에게 홀려 어머니가 죽고 아버지로부터 학대를 받다가 16살 때 집을 나간 후, 수십 년의 세월이 흘러 고명한 영매가 된 엘리스가 스펙스, 터커와 함께 미스테리 사냥꾼으로서 제령 활동을 하던 중. 어린 시절 그녀가 살던 뉴 멕시코의 집에 새로 이사 온 테드 가르자에게 도움을 요청 받아 수십 년 만에 그곳으로 돌아가면서 벌어지는 이야기다.',
}

@ns_movie.route('/movies/<string:name>')
class movie_list(Resource):
  # 영화 정보 조회
  def get(self, name):
    if not name in movie_info.keys():
      abort(404, description=f"Movie {name} doesn't exist")
    data = movie_info[name]

    return make_response(render_template('movies.html', movie_name=name, movie_info=data))


  # 새로운 영화 생성
  def post(self, name):
    if name in movie_info.keys():
      abort(409, description=f"Movie {name} already exists")

    movie_info[name] = dict()
    return Response(status=201)


  # 영화 정보 삭제
  def delete(self, name):
    if not name in movie_info.keys():
      abort(404, description=f"Movie {name} doesn't exists")
      
    del movie_info[name]
    return Response(status=200)


  # 영화 이름 변경
  def put(self, name):
    if not name in movie_info.keys():
      abort(404, description=f"Movie {name} doesn't exists")
    
    data = requset.get_json()
    movie_info[name] = params
    
    return Response(status=200)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

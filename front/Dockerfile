FROM node:latest

# 作業ディレクトリを/appに指定
WORKDIR /app
# vueCliをインストール
RUN npm install -g @vue/cli
RUN npm install --save @vue/cli-service
# 作業ディレクトリを/app/clientに指定
WORKDIR /app/client
# npmをインストール
RUN npm install
# context直下(docke-composeのコンテナfrontで指定されたディレクトリ)のstart.shをコンテナ内の/appフォルダにコピー
COPY ./start.sh /app/start.sh
# シェルを実行
CMD ["sh", "/app/start.sh"]
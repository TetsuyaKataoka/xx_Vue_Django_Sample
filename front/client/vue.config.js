module.exports = {
  configureWebpack: {
    devtool: 'source-map',
    devServer: {
      watchOptions: {
        poll: true
      },    
    },
  },

  transpileDependencies: ['vuetify'],

  pluginOptions: {
    i18n: {
      locale: 'en',
      fallbackLocale: 'en',
      localeDir: 'locales',
      enableInSFC: false,
    },
  },
}

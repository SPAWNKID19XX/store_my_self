import React from 'react';
import { WebView } from 'react-native-webview';

const StaticPage = () => {
  return (
    <WebView source={{ uri: 'http://localhost:3000/public/index.html' }} />
  );
};

export default StaticPage;
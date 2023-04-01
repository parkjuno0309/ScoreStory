import { React, useState } from 'react';
import logo from './logo.svg';
import './App.css';
import FeedPage from './components/FeedPage';
import MainLayout from './navigation/NavBar';
import PublishPage from './components/PublishPage';

import { useDbData } from './utilities/firebase'; 

import {
  createBrowserRouter, 
  createRoutesFromElements,
  Route, 
  RouterProvider
} from 'react-router-dom'

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route path="/" element={<MainLayout />}>
      {/* put more here */}
      <Route index element={<FeedPage />}/>
      <Route path="publishpage" element={<PublishPage />} />
    </Route>
  )
)

const App = () => {

  // const [data, error] = useDbData('/');
  // console.log(data);
  // if (data) {
  //   alert("YES");
  // } else {
  //   alert("NO");
  // }

  return (
    <RouterProvider router={router} />
  );
};

export default App;

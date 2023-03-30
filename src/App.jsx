import { React, useState } from 'react';
import logo from './logo.svg';
import './App.css';
import FeedPage from './components/FeedPage';
import MainLayout from './layouts/MainLayout';
import PublishPage from './components/PublishPage';

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
      <Route index element={<FeedPage />} />
      <Route path="publishpage" element={<PublishPage />} />
    </Route>
  )
)

const App = () => {

  return (
    <RouterProvider router={router} />
  );
};

export default App;

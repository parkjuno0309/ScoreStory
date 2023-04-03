import { React, useState } from 'react';
import logo from './logo.svg';
import './App.css';
import FeedPage from './components/FeedPage';
import MainLayout from './navigation/NavBar';
import PublishPage from './components/PublishPage';
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-icons/font/bootstrap-icons.css";

import { useDbData } from './utilities/firebase'; 

import { BrowserRouter, Route, Routes } from 'react-router-dom'

const App = () => {
  const [data, error] = useDbData("/");
  if (error) return <h1>Error loading data: {error.toString()}</h1>;
  if (data === undefined) return <h1>Loading data...</h1>;
  if (!data) return <h1>No data found</h1>;

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<MainLayout />}>
          {/* put more here */}
          <Route index element={<FeedPage posts={data.posts} />}/>
          <Route path="publishpage" element={<PublishPage posts={data.posts}/>} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
};

export default App;

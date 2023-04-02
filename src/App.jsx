import { React, useState } from 'react';
import logo from './logo.svg';
import './App.css';
import FeedPage from './components/FeedPage';
import MainLayout from './navigation/NavBar';
import PublishPage from './components/PublishPage';

import { useDbData } from './utilities/firebase'; 

import {
  BrowserRouter,
  createBrowserRouter, 
  createRoutesFromElements,
  Route, 
  Routes,
  RouterProvider
} from 'react-router-dom'

// const router = createBrowserRouter(
//   createRoutesFromElements(
//     <Route path="/" element={<MainLayout />}>
//       {/* put more here */}
//       <Route index element={<FeedPage />}/>
//       <Route path="publishpage" element={<PublishPage posts={data.posts}/>} />
//     </Route>
//   )
// )

const App = () => {
  const [data, error] = useDbData("/");
  if (error) return <h1>Error loading data: {error.toString()}</h1>;
  if (data === undefined) return <h1>Loading data...</h1>;
  if (!data) return <h1>No data found</h1>;

  // const [data, error] = useDbData('/');
  // console.log(data);
  // if (data) {
  //   alert("YES");
  // } else {
  //   alert("NO");
  // }

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<MainLayout />}>
          {/* put more here */}
          <Route index element={<FeedPage />}/>
          <Route path="publishpage" element={<PublishPage posts={data.posts}/>} />
        </Route>
      </Routes>
    </BrowserRouter>
    // <RouterProvider router={router} data={data}/>
  );
};

export default App;

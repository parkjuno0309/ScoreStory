import { useState } from 'react';
import logo from './logo.svg';
import './App.css';
import FeedPage from './components/FeedPage';

const App = () => {
  const examplePost = [{
    "name": "Alex",
    "email": "alexmodugno2024@u.northwestern.edu",
    "item": "Toaster",
    "date": "3/3/23",
    "time": "5pm-6pm"
  },
  {
    "name": "Emily",
    "email": "emily2024@u.northwestern.edu",
    "item": "Toaster",
    "date": "3/3/23",
    "time": "5pm-6pm"
  }];

  return (
    <div className="App">
      <header className="App-header">
        <FeedPage allPosts={examplePost} />
      </header>
    </div>
  );
};

export default App;

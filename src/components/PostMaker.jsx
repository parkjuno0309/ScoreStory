import { useDbUpdate } from '../utilities/firebase'
import { useState } from 'react';
import "./PostMaker.css";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-icons/font/bootstrap-icons.css";

const PostMaker = ({ posts }) => {
    // console.log(posts)
    let post_id;
    if(!posts){
        post_id = 1;
    }
    else{
        post_id = posts.length;
    }
    const [update, result] = useDbUpdate(`/posts/${post_id}`);

    const submit = (e) => {
        // console.log(e.target[3].value)
        if(e.target[0].value === ''){}
        else{
        e.preventDefault();
        update({
            name: e.target[0].value,
            id: post_id,
            email: e.target[1].value,
            item: e.target[2].value,
            date: e.target[3].value,
            startTime: e.target[4].value, 
            endTime: e.target[5].value 
        });
        document.getElementById('post-form').reset();
    }};
        
        
    return (
      <form onSubmit={submit} id="post-form" className="form-group row">
        <input className="py-2 mt-2" placeholder="Name" />
        <input className="py-2 mt-2" placeholder="Email" />
        <input className="py-2 mt-2" placeholder="Item" />
        <div className="py-2 mt-2">
          <label>Date</label>
          <input type="date" placeholder="Date" />
        </div>
        <div className="py-2 mt-2">
          <label>Time</label>
          <input className="py-2 mt-2" type="time" placeholder="Start Time" />
          <input className="py-2 mt-2 ml-3" type="time" placeholder="End Time" />
        </div>
        <button className="btn btn-primary" type="submit">
          Post
        </button>
      </form>
    );
};

export default PostMaker;
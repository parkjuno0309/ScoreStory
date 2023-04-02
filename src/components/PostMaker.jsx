import { useDbUpdate } from '../utilities/firebase'
import { useState } from 'react';
import "./PostMaker.css";

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
        <form onSubmit={submit} id="post-form">
            <input className="form-question" placeholder="Name" />
            <input className="form-question" placeholder="Email" />
            <input className="form-question" placeholder="Item" />
            <div className="form-question">
                <label>Date</label>
                <input type="date" placeholder="Date" />
            </div>
            <div className="form-question">
                <label>Time</label>
                <input type="time" placeholder="Start Time" />
                <input type="time" placeholder="End Time" />
            </div>
            <button type="submit">Post</button>
        </form>
    )
};

export default PostMaker;
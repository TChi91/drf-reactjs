import React, { useState, useEffect } from "react";
import { useForm } from "react-hook-form";
import { API, postMessage, deleteMessage } from "../../api/api";
import img from "../../assets/hro.png";

const Messages = () => {
	const { register, handleSubmit } = useForm();
	const [msgList, setMsgList] = useState([]);
	const onSubmit = (data) => postMessage(data);

	useEffect(() => {
		API.get("messages/").then((response) => setMsgList(response.data));
	}, [onSubmit]);

	return (
		<div className="hello">
			<img src={img} style={{ width: 250 }} />
			<p>The data below is added/removed from the SQLite Database using Django's ORM and Rest Framework.</p>
			<br />

			<form onSubmit={handleSubmit(onSubmit)}>
				<label>Subject</label>
				<br></br>
				<input type="text" placeholder="Hello" name="subject" ref={register({ required: true })} />
				<br></br>
				<br></br>
				<br></br>
				<label>Message</label>
				<br></br>
				<input type="text" placeholder="From the other side" name="body" ref={register} />
				<br></br>
				<br></br>
				<input type="submit" />
			</form>

			<hr />
			<h3>Messages on Database</h3>

			{msgList.length === 0 ? (
				<p>No Messages</p>
			) : (
				msgList.map((msg, index) => {
					return (
						<div className="msg" key={msg.id}>
							<br></br>
							<span>{index}</span> | <span className="msg-subject"> {msg.subject}</span>
							<br></br>
							<span className="msg-subject" onClick={() => deleteMessage(msg.id)}>
								X
							</span>
							<span className="msg-body"> | {msg.body}</span>
							<hr></hr>
						</div>
					);
				})
			)}
		</div>
	);
};

export default Messages;

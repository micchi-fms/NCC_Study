var app=new Vue({
	data:{
		title: "Todo App Title",
		taskList:[
			{ text: "todo", isDone: false },
			{ text: "todo01", isDone: false },
			{ text: "todo02", isDone: false },
			{ text: "todo03", isDone: true },
		],
		newTaskText: "",
	},
	methods:{
		addTask:function(){
			var newTask={
				text:this.newTaskText,
				isDone:false,
			};
			this.taskList.push(newTask);
			this.newTaskText="";
		},
	},
});

// [].push({key:"value"});

//vueはデータバインディングする言語
//データがあってそれをhtmlにバインドする
//どこの要素に(jsからのhtml)マウントするか
app.$mount("#app");
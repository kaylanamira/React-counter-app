import React, { Component } from 'react';

class Counter extends Component {
    state = {
        value : this.props.value
        //tags : []
    };

    // constructor() {
    //     super(); //super is needed in order to construct
    //     this.handleIncrement = this.handleIncrement.bind(this);
    // };

    handleIncrement = (product) => {
        //this can only be used if there's a constructor
        console.log(product);
        this.setState({value: this.state.value + 1 });
    }
    //alternatives without constructor is handleIncrement = () => {}
    //children is specified by Fragment
    //span is used for inline embedding
    // renderTags() {
    //     if (this.state.tags.length === 0) return <p>No</p>;
    //     return <ul>{this.state.tags.map(arrElement => <li key={arrElement}>{arrElement}</li>)}</ul>
    // };


    render() { 
        return (
            <div> 
                <span className={this.getBadgeClasses()}>{this.formatCount()}</span>
                <button onClick={() => this.handleIncrement({ id : 1 }) }>Increment</button> 

                {/* <ul>
                    {this.state.tags.map(arrElement => <li key={arrElement}>{arrElement}</li>)}
                </ul>
                {/* Conditional rendering using truthsies, first expression is boolean, if it is true the next will also be rendered */}
                {/* {this.state.tags.length === 0 && "Please create a new tag!"}
                {this.renderTags()} */}
            </div>
        );
    }  
    getBadgeClasses() {
        //renders dynamically
        let classes = "badge m-2 badge-";
        let hitung = this.state.value;
        classes += (hitung === 0) ? "warning" : "primary";
        return classes;
    }

    formatCount() {
        const {value} = this.state;
        return value === 0? 'Zero' : value;
    }
    
}  

export default Counter;
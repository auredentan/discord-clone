import { createMachine, assign, spawn } from 'xstate'
import { createSubredditMachine } from './subredditMachine'

export interface RedditMachineContext {
	subreddit?: any
	subreddits: any
}

export type RedditMachineEvent = {
	type: 'SELECT'
	name: string
}

const redditMachine = createMachine<RedditMachineContext, RedditMachineEvent>(
	{
		id: 'reddit',
		initial: 'idle',
		context: {
			subreddit: null,
			subreddits: {},
		},
		states: {
			idle: {},
			selected: {}, // no invocations!
		},
		on: {
			SELECT: {
				target: '.selected',
				actions: ['subr'],
			},
		},
	},
	{
		actions: {
			subr: assign((context, event) => {
				let subreddit = context.subreddits[event.name]

				if (subreddit) {
					return {
						...context,
						subreddit,
					}
				}

				console.log("event", event)

				// Otherwise, spawn a new subreddit actor and
				// save it in the subreddits object
				subreddit = spawn(createSubredditMachine(event.name))
				return {
					subreddits: {
						...context.subreddits,
						[event.name]: subreddit,
					},
					subreddit,
				}
			}),
		},
	}
)

export { redditMachine }

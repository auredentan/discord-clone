import axios from 'axios'
import { createMachine, assign } from 'xstate'

export interface SubRedditMachineContext {
	subreddit: string
	posts?: any[]
	lastUpdated: any
}

export type SubRedditMachineEvent =
	| {
			type: 'REFRESH'
	  }
	| {
			type: 'RETRY'
	  }

function invokeFetchSubreddit(context: SubRedditMachineContext) {
	const { subreddit } = context

	return axios
		.get(`https://www.reddit.com/r/${subreddit}.json`)
		.then((json) => {
			return json.data.data.children.map((child) => child.data)
		})
}

const createSubredditMachine = (subreddit: string) => {
	return createMachine<SubRedditMachineContext, SubRedditMachineEvent>(
		{
			id: 'subreddit',
			initial: 'loading',
			context: {
				subreddit, // subreddit name passed in
				posts: null,
				lastUpdated: null,
			},
			states: {
				loading: {
					invoke: {
						id: 'fetch-subreddit',
						src: invokeFetchSubreddit,
						onDone: {
							target: 'loaded',
							actions: ['posts', 'lastUpdated'],
						},
						onError: 'failure',
					},
				},
				loaded: {
					on: {
						REFRESH: 'loading',
					},
				},
				failure: {
					on: {
						RETRY: 'loading',
					},
				},
			},
		},
		{
			actions: {
				posts: assign((_, event: any) => {
					return { posts: event.data }
				}),
				lastUpdated: assign(() => ({ lastUpdated: Date.now() })),
			},
            guards: {},
            services: {}
		}
	)
}

export { createSubredditMachine }
